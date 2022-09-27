import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2', region_name='us-east-1')
    ec2=client.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ['g4dn.xlarge']},
                                       {'Name': 'instance-state-name', 'Values': ['running']}])
    ec2stopped=client.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ['g4dn.xlarge']},
                                       {'Name': 'instance-state-name', 'Values': ['stopped']}])
    value=["Running instances:"]
    stopped=["Stoped instances:"]
    for pythonins in ec2['Reservations']:
        for printout in pythonins['Instances']:
            for dns in pythonins['Instances']:
                for printname in printout['Tags']:
                    print(printname['Value'])
                    print(printout['InstanceId'])
                    print(dns['PublicIpAddress'])
                    add=[printname['Value'],printout['InstanceId'],dns['PublicIpAddress']]
                    value.extend(add)
    for stoppedins in ec2stopped['Reservations']:
        for printstop in stoppedins['Instances']:
            for dnsstop in stoppedins['Instances']:
                for printnamestop in printstop['Tags']:
                    print(printnamestop['Value'])
                    print(printstop['InstanceId'])
                    addstop=[printnamestop['Value'],printstop['InstanceId']]
                    stopped.extend(addstop)

    return (value, stopped)