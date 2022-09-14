import boto3

def lambda_handler(event, context):
    client = boto3.resource('ec2', region_name='us-east-1')
    instances = client.create_instances(
        ImageId="ami-0dea20a5de7a84a50",
        MinCount=1,
        MaxCount=1,
        InstanceType="g4dn.xlarge",
        KeyName="key_name",
        SecurityGroupIds=["sg-03e745d4a67ee46b2"],
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Instance-Name'
                },
            ]
        },
    ]
    )
    return("Instance launched!")
