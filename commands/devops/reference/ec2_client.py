import boto3

# Create an EC2 resource
ec2 = boto3.client("ec2")

# Retrieve running instances
response = ec2.describe_instances(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])

# Extract instance IDs
instances = []
# Iterates over each reservation block.
for reservation in response["Reservations"]:
    # Iterates over each instance inside a reservation.
    for instance in reservation["Instances"]:
        # adds the Instance ID to the instances list.
        instances.append(instance["InstanceId"])

# Print the active instance IDs
print("Running Instances:", instances)
