# Python-AWS_Lambda-API_Gateway_EC2-instances
AWS Lambda functions on python to control (list, create, terminate, start, stop and reboot) EC2 instances over API Gateway
### Add role to lambda function

### Making a new function in AWS Lambda
1. Go to AWS console in services Lambda and press button "Create function"
![Create function](/img/create-function.jpg)
Fill all fileds like on a screenshot below:
- Name - `name of your function`
- Runtime - `Python 3.9`
- Click to collapse `Change default execution role`
- Select `Use an existing role`
- Select your lambda function role with permissions to Full access EC2 instances
![role function1](/img/role-function1.jpg)
![role function2](/img/role-function2.jpg)
2. Copy code of your function in tab `Code` and press `Deploy`.
For example - code to start, stop, reboot and terminate instances (change `region name` if you need):
```python
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
```
![Insert code function](/img/insert-code-function.jpg)
3. Test your function.
Go to the Test tab and `Create new event`, in `Event JSON` field add (change `id_instance` to your instance ID and `start` to what you need):
```json
{
    "instanceid": "id_instance",
    "state": "start"
}
```
![Test function](/img/test-function.jpg)
And then click to `Save` and `Test`.
![Test function details](/img/test-function-details.jpg)
Execution result must be succeeded, and you will see something like on screenshot.
### Create an API Gateway to your function
Let's create an access point to the `Lambda function` created above and additionally set protection against unwanted launches using the `API Key`

Go to the `AWS API Gateway service`. Click on the `Create API` button, set the name of the API.
![Create API](/img/create-api.jpg)
![Create API2](/img/create-api2.jpg)
We add the GET method to the newly created API. To do this, select Actions --> Create method, in the drop-down list that appears, select the GET method and click on the checkmark
![Create Method](/img/api-create-method.jpg)
![Create Method GET](/img/api-create-method-get.jpg)
Next, we indicate that our `Lambda function` will be used in the `GET` method. Select it and click on the `Save` button.
![Link lambda function](/img/api-function-link.jpg)
Let's deploy our `API`, thereby obtaining a `URL` to call the `API`.
Click `Actions` --> `Deploy API`, and then Deployment stage --> `New Stage`.
<details>
<summary>Click this to collapse/fold.</summary>

![Deploy lambda function](/img/api-deploy.jpg)
![Deploy lambda function 2](/img/api-deploy2.jpg)

</details>

> It is possible to deploy the `API` to different stages and call these stages whatever you like (for example, DEV/QA/PROD). We will deploy immediately to `PROD`
