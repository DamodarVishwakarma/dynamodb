import boto3
from botocore.exceptions import ClientError
dynamodb = boto3.client('dynamodb')

def create_item():
    try:
        response = dynamodb.put_item(
            TableName='Customer',
            Item={
                'Id': {'N': '6'},
                'Name': {'S': 'Shubhman'},
                'Age': {'N': '22'}
            }
        )
        print("Item created successfully:", response)
    except ClientError as e:
        print("Error creating item:", e)
create_item()
