import boto3
from botocore.exceptions import ClientError
dynamodb = boto3.client('dynamodb')

table_name = 'Customer'
page_size = 2 
offset = 2 

try:
    # Scan the table with limit and exclusive start key
    response = dynamodb.scan(
        TableName=table_name,
        Limit=page_size,
        ExclusiveStartKey={'Id': {'N': str(offset)}}
    )
    items = response['Items']

    while 'LastEvaluatedKey' in response:
        response = dynamodb.scan(
            TableName=table_name,
            Limit=page_size,
            ExclusiveStartKey=response['LastEvaluatedKey']
        )
        items.extend(response['Items'])
    for item in items:
        print(item)

except ClientError as e:
    print("Error scanning table:", e)