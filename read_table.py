import boto3
from botocore.exceptions import ClientError
dynamodb = boto3.client('dynamodb')

table_name = 'Customer'

try:
    response = dynamodb.scan(TableName=table_name)
    items = response['Items']

    while 'LastEvaluatedKey' in response:
        response = dynamodb.scan(
            TableName=table_name,
            ExclusiveStartKey=response['LastEvaluatedKey']
        )
        items.extend(response['Items'])
    for item in items:
        print(item)

except ClientError as e:
    print("Error scanning table:", e)