import click
import boto3
import sys
from pathlib import Path
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datetime import datetime, timedelta

# Get current script directory
currentdir = Path(__file__).resolve().parent
# Get parent directory
parentdir = currentdir.parent
# Add parent directory to sys.path
sys.path.insert(0, str(parentdir))

# import logger after specifying root/parent path
import logger

# ====================

import boto3
from datetime import datetime, timedelta, timezone

# Initialize AWS clients
ec2 = boto3.client("ec2")
cloudwatch = boto3.client("cloudwatch")

# Get all running EC2 instances
response = ec2.describe_instances(Filters=[{"Name": "instance-state-name", "Values": ["terminated"]}])

# Extract instance IDs
instances = []
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instances.append(instance["InstanceId"])

# Function to get CloudWatch metrics
def get_metric(instance_id, metric_name, namespace="AWS/EC2", statistic="Average"):
    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
        StartTime=datetime.now(timezone.utc) - timedelta(minutes=30),  # Increased time window
        EndTime=datetime.now(timezone.utc),
        Period=300,  # 5-minute intervals
        Statistics=[statistic]
    )
    datapoints = response.get("Datapoints", [])
    return datapoints[-1][statistic] if datapoints else "No Data"

# Fetch and print metrics for each instance
for instance_id in instances:
    cpu_utilization = get_metric(instance_id, "CPUUtilization")
    disk_read_bytes = get_metric(instance_id, "DiskReadBytes")
    disk_write_bytes = get_metric(instance_id, "DiskWriteBytes")
    network_in = get_metric(instance_id, "NetworkIn")
    network_out = get_metric(instance_id, "NetworkOut")
    status_check = get_metric(instance_id, "StatusCheckFailed")

    print(f"Instance: {instance_id}")
    print(f"  CPU Utilization: {cpu_utilization}%")
    print(f"  Disk Read (Bytes): {disk_read_bytes}")
    print(f"  Disk Write (Bytes): {disk_write_bytes}")
    print(f"  Network In (Bytes): {network_in}")
    print(f"  Network Out (Bytes): {network_out}")
    print(f"  Instance Status Check Failed: {status_check}")
    print("-" * 40)
