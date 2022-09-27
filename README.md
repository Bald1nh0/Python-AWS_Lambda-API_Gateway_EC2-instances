# Python-AWS_Lambda-API_Gateway_EC2-instances
AWS Lambda functions on python to control (list, create, terminate, start, stop and reboot) EC2 instances over API Gateway
### Add role to lambda function

### Making a new function in AWS Lambda
1. Go to AWS console in services Lambda and press button "Create function"
<details>
<summary>Create function</summary>

![Create function](/img/create-function.jpg)

</details>

Fill all fileds like on a screenshot below:
- Name - `name of your function`
- Runtime - `Python 3.9`
- Click to collapse `Change default execution role`
- Select `Use an existing role`
- Select your lambda function role with permissions to Full access EC2 instances
<details>
<summary>Role function</summary>

![role function1](/img/role-function1.jpg)
![role function2](/img/role-function2.jpg)

</details>

2. Copy code of your function in tab `Code` and press `Deploy`.
For example - code to start, stop, reboot and terminate instances (change `region name` if you need)
<details>
<summary>Code</summary>

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

</details>

<details>
<summary>Insert code function</summary>

![Insert code function](/img/insert-code-function.jpg)

</details>

3. Test your function.
Go to the Test tab and `Create new event`, in `Event JSON` field add (change `id_instance` to your instance ID and `start` to what you need):
```json
{
    "instanceid": "id_instance",
    "state": "start"
}
```
<details>
<summary>Test Function</summary>

![Test function](/img/test-function.jpg)

</details>

And then click to `Save` and `Test`.
<details>
<summary>Test result</summary>

![Test function details](/img/test-function-details.jpg)

</details>

Execution result must be succeeded, and you will see something like on screenshot.
### Create an API Gateway to your function
Let's create an access point to the `Lambda function` created above and additionally set protection against unwanted launches using the `API Key`

Go to the `AWS API Gateway service`. Click on the `Create API` button, set the name of the API.
<details>
<summary>Create API</summary>

![Create API](/img/create-api.jpg)
![Create API2](/img/create-api2.jpg)

</details>

We add the GET method to the newly created API. To do this, select Actions --> Create method, in the drop-down list that appears, select the GET method and click on the checkmark
<details>
<summary>Create method</summary>

![Create Method](/img/api-create-method.jpg)
![Create Method GET](/img/api-create-method-get.jpg)

</details>

Next, we indicate that our `Lambda function` will be used in the `GET` method. Select it and click on the `Save` button.
<details>
<summary>Link lambda function</summary>

![Link lambda function](/img/api-function-link.jpg)

</details>

###### Deploy function
Let's deploy our `API`, thereby obtaining a `URL` to call the `API`.
Click `Actions` --> `Deploy API`, and then Deployment stage --> `New Stage`.
<details>
<summary>Deploy function</summary>

![Deploy lambda function](/img/api-deploy.jpg)
![Deploy lambda function 2](/img/api-deploy2.jpg)

</details>

> It is possible to deploy the `API` to different stages and call these stages whatever you like (for example, DEV/QA/PROD). We will deploy immediately to `PROD`

Add support for request parameters to the `API`

Go to the GET request settings and go to the Method Request step

<details>
<summary>Method request</summary>

![Method request](/img/api-method-request.jpg)

</details>

In the detailed settings of the `Method Request`, you need to expand the `URL Query String Parameters` block and add a new `instanceid` and `state` parameter and make it `Required`:
<details>
<summary>URL Query String Parameters</summary>

![URL Query String Parameters](/img/api-add-url-query.jpg)

</details>

We return to the `Method Execution` page and go to the `Integration Request`. We go down to the very bottom of the page and open the `Mapping Templates` block. Select `When there are no templates defined (recommended)`, specify `application/json` in the `Content-Type` field and click on the checkmark. Scroll down the page and enter the code in the text field, as shown in the picture below. After that, click on the `Save` button.
<details>
<summary>Method Execution</summary>

![Method Execution](/img/api-integration-request.jpg)
![Mapping Templates](/img/api-mapping-templates.jpg)
```json
{
    "instanceid" : "$input.params('instanceid')",
    "state" : "$input.params('state')"
}
```

</details>

It remains only to protect our `API` from unwanted attacks from the outside.

To do this, you need to configure the `API` in such a way that, when accessed, it requires a `secret key`, which is passed in the `header`.

Let's go to the `Keys API` and create a new `API key` binding.
<details>
<summary>API Keys</summary>

![API Keys](/img/api-key-create.jpg)

</details>

After the `API Key` has been successfully created, you must specify that the `API` must require the mandatory transmission of the `API key` in the `request header`. And bind a `specific key` to the `API`.

Let's go back to the `GET request settings` in the `Method Request` and change the `API Key Required parameter` from `false` to `true`. The `API` will now require an `API Key` to be passed.
<details>
<summary>API Key true</summary>

![API Key true](/img/api-key-true.jpg)

</details>

Go to `Usage Plan` and create a new `API usage plan`.

Firstly, we will give it a `name` and `description`, and secondly, here you can also set limits on the launch of the `API`, for example, no more than one launch per second, etc.
<details>
<summary>Create Usage Plan</summary>

![Create Usage Plan](/img/api-usage-plan.jpg)

</details>

Click on `Next` and go to the next page, where you need to associate the `API stages` with the `usage plan`
<details>
<summary>Associate API stages</summary>

![Associate API stages](/img/api-link-to-usage-plan.jpg)

</details>

On the next page, we bind `API Keys` to the `API usage plan`. Click on the `Add API Keys to Usage Plan` button and find the `API Keys` created in the previous steps by name
<details>
<summary>Add API Keys to Usage Plan</summary>

![Add API Keys to Usage Plan](/img/api-add-api-key-to-usage-plan.jpg)

</details>

[Deploy](#deploy-function) your `function` and test it with `Postman`

<details>
<summary>Test your function</summary>

![Test your function](/img/postman-check.jpg)

</details>