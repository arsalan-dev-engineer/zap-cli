import click
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from pathlib import Path
import sys

# Get current script directory
currentdir = Path(__file__).resolve().parent
# Get parent directory
parentdir = currentdir.parent
# Add parent directory to sys.path
sys.path.insert(0, str(parentdir))

# import logger after specifying root/parent path
import logger

# ========== INITIALIZE AWS EC2 CLIENT

def get_ec2_client(region=None):
    """
    Returns a Boto3 EC2 client using the default profile.
    """
    try:
        return boto3.client("ec2", region_name=region)
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"Error: {str(e)}")
        exit(1)

# ========== EC2 INSTANCE CLEANER

def clean_unused_instances(ec2_client):
    """
    Find and terminate unused EC2 instances.
    """
    logger.info("\n==================== EC2 INSTANCE CLEANUP")
    instances = ec2_client.describe_instances()
    terminated_instances = []

    total_instances = 0
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            launch_time = instance["LaunchTime"]

            total_instances += 1
            # Display instance details
            click.echo(f"\n===== INSTANCE: {total_instances}")
            click.echo(f"Instance ID: {instance_id}")
            click.echo(f"State      : {state}")
            click.echo(f"Launch time: {launch_time.strftime('%Y-%m-%d %H:%M:%S')}")

            if state == "stopped":
                click.echo(f"Status: {state} - Terminating instance...")
                ec2_client.terminate_instances(InstanceIds=[instance_id])
                terminated_instances.append(instance_id)
            else:
                click.echo(f"Status: {state} - No action needed.")

    if terminated_instances:
        logger.info(f"\nTerminated instances: {', '.join(terminated_instances)}")
    else:
        logger.info("\nNo stopped instances to terminate.")

# ========== CLEAN UNUSED VOLUMES

def clean_unused_volumes(ec2_client):
    """
    Find and delete unused EC2 volumes.
    """
    click.echo("\n==================== EC2 VOLUME CLEANUP")
    volumes = ec2_client.describe_volumes()
    deleted_volumes = []

    total_volumes = 0
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        state = volume['State']
        attachment_state = volume.get('Attachments', [])
        creation_time = volume['CreateTime']

        total_volumes += 1
        # Display instance details
        click.echo(f"\n===== INSTANCE: {total_volumes}")
        # Display volume details
        click.echo(f"Volume ID  : {volume_id}")
        click.echo(f"State      : {state}")
        click.echo(f"Created on : {creation_time.strftime('%Y-%m-%d %H:%M:%S')}")
        if attachment_state:
            click.echo(f"Attached to : {', '.join([attachment['InstanceId'] for attachment in attachment_state])}")
        else:
            click.echo("Attached to : None (Unattached)")

        if state == 'available' and not attachment_state:
            click.echo(f"Status: Unattached — Deleting this volume...")
            ec2_client.delete_volume(VolumeId=volume_id)
            deleted_volumes.append(volume_id)
        else:
            click.echo(f"Status: In Use — No action needed.")

    if deleted_volumes:
        click.echo(f"\nDeleted volumes: {', '.join(deleted_volumes)}\n")
    else:
        click.echo("\nNo unattached volumes to delete.\n")

# ========== CLICK GROUP

@click.group(help="A group of commands for EC2 instance cleanup")
def ec2_cleaner():
    """
    A group of commands for terminating EC2 instances & volumes.
    """
    pass


@ec2_cleaner.command()
@click.option('--region', default=None, help='AWS region to target (default is configured region)')
def clean_instances(region):
    """
    Find and terminate unused EC2 instances.
    """
    ec2_client = get_ec2_client(region)
    clean_unused_instances(ec2_client)


@ec2_cleaner.command()
@click.option('--region', default=None, help='AWS region to target (default is configured region)')
def clean_volumes(region):
    """
    Find and delete unused EC2 volumes.
    """
    ec2_client = get_ec2_client(region)
    clean_unused_volumes(ec2_client)


@ec2_cleaner.command()
@click.option('--region', default=None, help='AWS region to target (default is configured region)')
def clean_all(region):
    """
    Clean both unused EC2 instances and volumes.
    """
    ec2_client = get_ec2_client(region)
    clean_unused_instances(ec2_client)
    clean_unused_volumes(ec2_client)


# if this script is run directly, invoke the 'ec2_cleaner' group
if __name__ == "__main__":
    ec2_cleaner()
