import boto3
from botocore.exceptions import ClientError
dynamodb = boto3.client('dynamodb')

def create_table():
    try:
        response = dynamodb.create_table(
            TableName='Customer',
            KeySchema=[
                {
                    'AttributeName': 'Id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'Id',
                    'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        print("Table created successfully:", response)
    except ClientError as e:
        print("Error creating table:", e)

create_table()