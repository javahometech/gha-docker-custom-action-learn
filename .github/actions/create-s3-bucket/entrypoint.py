import boto3
import os

bucket_name = os.getenv("BUCKET_NAME")
region = os.getenv("REGION")

if not bucket_name:
    raise Exception("BUCKET_NAME not provided")

print(f"Creating bucket: {bucket_name} in region: {region}")

s3 = boto3.client("s3", region_name=region)

try:
    if region == "us-east-1":
        # Special rule: us-east-1 cannot include LocationConstraint
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": region}
        )
    print("Bucket created successfully!")
except Exception as e:
    print(f"Failed: {e}")
    exit(1)
