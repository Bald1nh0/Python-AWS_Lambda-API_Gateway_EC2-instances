import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('ec2', region_name='us-east-1')
    instanceid = (event['instanceid'])
    response = client.reboot_instances(
        InstanceIds=[
            instanceid,
        ],
    )
    return (response)