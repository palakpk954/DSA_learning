import boto3

class AWSController:
    def __init__(self):
        self.ec2 = boto3.client('ec2', region_name='us-east-1')
        self.sns = boto3.client('sns', region_name='us-east-1')
        self.topic_arn = 'arn:aws:sns:us-east-1:123456789012:GestureNotifications'

    def launch_instance(self):
        response = self.ec2.run_instances(
            ImageId='ami-0abcdef1234567890',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"EC2 Instance Launched: {instance_id}")
        self.send_notification(f"EC2 Instance {instance_id} Launched")

    def terminate_instances(self):
        instances = self.ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        ids = [inst['InstanceId'] for res in instances['Reservations'] for inst in res['Instances']]

        if not ids:
            print("No instances running.")
            return

        self.ec2.terminate_instances(InstanceIds=ids)
        print("Terminated instances:", ids)
        self.send_notification(f"Terminated instances: {ids}")

    def send_notification(self, message):
        self.sns.publish(
            TopicArn=self.topic_arn,
            Message=message,
            Subject="AWS Gesture Automation Update"
        )
