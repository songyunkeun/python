# Manual Steps to see/list all iam users:
# ========================================
#   step1: Get AWS Management Console
#   Step2: Get IAM Console
#          Options: Users, Groups, roles......
# ========================================
import boto3

aws_mag_con=boto3.session.Session(profile_name="default")
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)

#========================================
# import boto3
# aws_mag_con=boto3.session.Session(profile_name="default")
# s3_con=aws_mag_con.resource('s3')

