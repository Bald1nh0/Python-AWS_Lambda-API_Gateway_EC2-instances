import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2', region_name='us-east-1')
    ec2=client.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ['g4dn.xlarge']},
                                       {'Name': 'instance-state-name', 'Values': ['running']}])
    value=[]
    for pythonins in ec2['Reservations']:
        for printout in pythonins['Instances']:
            for dns in pythonins['Instances']:
                for printname in printout['Tags']:
                    print(printname['Value'])
                    print(printout['InstanceId'])
                    print(dns['PublicIpAddress'])
                    add=[printname['Value'],printout['InstanceId'],dns['PublicIpAddress']]
                    value.extend(add)

    return (value )