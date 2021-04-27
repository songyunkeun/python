import boto3

aws_mag_con=boto3.session.Session(profile_name='root')
aws_sts_client=aws_mag_con.client(service_name='sts')

response = aws_sts_client.get_caller_identity()
#response = aws_sts_client.get_access_key_info(AccessKeyId='AKIAXYJ3XGPAEIFGB4VM')
print(response)


#{'UserId': 'AIDAIMYNZVJ3E2GXMANNQ', 'Account': '533238068160', 'Arn': 'arn:aws:iam::533238068160:user/syk',
 