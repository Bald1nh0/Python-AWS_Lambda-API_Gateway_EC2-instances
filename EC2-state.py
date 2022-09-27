import boto3
import json

def lambda_handler(event, context):
    state = (event['state'])
    if state == "start":
        client = boto3.client('ec2', region_name='us-east-1')
        instanceid = (event['instanceid'])
        response = client.start_instances(
            InstanceIds=[
                instanceid,
            ],
        )
    elif state == "stop":
        client = boto3.client('ec2', region_name='us-east-1')
        instanceid = (event['instanceid'])
        response = client.stop_instances(
            InstanceIds=[
                instanceid,
            ],
        )
    elif state == "reboot":
        client = boto3.client('ec2', region_name='us-east-1')
        instanceid = (event['instanceid'])
        response = client.reboot_instances(
            InstanceIds=[
                instanceid,
            ],
        )
    elif state == "terminate":
        client = boto3.client('ec2', region_name='us-east-1')
        instanceid = (event['instanceid'])
        response = client.terminate_instances(
            InstanceIds=[
                instanceid,
            ],
        )
    return (response)