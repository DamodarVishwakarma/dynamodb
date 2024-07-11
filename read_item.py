import boto3
from botocore.exceptions import ClientError
dynamodb = boto3.client('dynamodb')

def read_item():
    try:
        response = dynamodb.get_item(
            TableName='Customer',
            Key={
                'Id': {'N': '1'}
            }
        )
        item = response.get('Item')
        if item:
            print("Retrieved item:", item)
        else:
            print("Item not found")
    except ClientError as e:
        print("Error reading item:", e)

read_item()
