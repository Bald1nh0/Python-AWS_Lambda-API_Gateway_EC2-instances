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
