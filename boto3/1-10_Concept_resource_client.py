# Manual Steps to see/list all iam users:
# ========================================
#   step1: Get AWS Management Console
#   Step2: Get IAM Console
#          Options: Users, Groups, roles......
# ========================================
import boto3

aws_mag_con=boto3.session.Session(profile_name="default")
iam_con_resource=aws_mag_con.resource(service_name='iam', region_name='ap-northeast-2')
# iam_con_client=aws_mag_con.client(service_name='iam')
# # print(dir(aws_mag_con))
# # print(aws_mag_con.get_available_resources)
#
for each_user in iam_con_resource.users.all(): # Resource는 List
    print(each_user)    # .attribute: arn, create_date, password_last_used, path, permissions_boundary,tags, user_id,user_name

# for each_user in iam_con_client.list_users()['Users']:  # client는 Dictionary.  항목은 resource의 attribute와 비슷
#     print(each_user)

#========================================
# aws_mag_con=boto3.session.Session(profile_name="default")
# ec2_con_resource=boto3.resource(service_name='ec2')
# ec2_con_client=aws_mag_con.client(service_name='ec2')
# for each_ec2 in ec2_con_resource.instances.all():
#     print(each_ec2)   # .attribute: 매우 많다

# for each_ec2 in ec2_con_client.describe_instances()['Reservations']:    # client는 Dictionary
#     for each in each_ec2['Instances']:
#         print(each['InstanceId'])




## print(dir(aws_mag_con))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', '__weakref__', '_loader', '_register_default_handlers', '_session', '_setup_loader',
#  'available_profiles', 'client', 'events', 'get_available_partitions', 'get_available_regions',
#  'get_available_resources', 'get_available_services', 'get_credentials', 'profile_name', 'region_name',
#  'resource', 'resource_factory']

# print(aws_mag_con.get_available_resources())
# ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']

