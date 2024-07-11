import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

response = table.get_item(
    Key={
        'id': 1
    }
)
item = response['Item']
print(item)

# IN

response = table.scan(
    FilterExpression=Attr('attribute_name').is_in(['value1', 'value2', 'value3'])
)
items = response['Items']
for item in items:
    print(item)


# ILIKE

response = table.scan(
    FilterExpression=Attr('attribute_name').begins_with('value')
)
items = response['Items']
for item in items:
    print(item)

# CONTAINS

response = table.scan(
    FilterExpression=Attr('attribute_name').contains('substring')
)
items = response['Items']
for item in items:
    print(item)

# NOT CONTAINS

response = table.scan(
    FilterExpression=Attr('attribute_name').not_contains('substring')
)
items = response['Items']
for item in items:
    print(item)

# GT

response = table.scan(
    FilterExpression=Attr('attribute_name').gt(10)
)
items = response['Items']
for item in items:
    print(item)

# LE

response = table.scan(
    FilterExpression=Attr('attribute_name').lte(100)
)
items = response['Items']
for item in items:
    print(item)

# GOE

response = table.scan(
    FilterExpression=Attr('attribute_name').gte(50)
)
items = response['Items']
for item in items:
    print(item)

# LET

response = table.scan(
    FilterExpression=Attr('attribute_name').lt(200)
)
items = response['Items']
for item in items:
    print(item)

# IS EMPLTY

response = table.scan(
    FilterExpression=Attr('attribute_name').not_exists()
)
items = response['Items']
for item in items:
    print(item)

# IS NOT EMPTY

response = table.scan(
    FilterExpression=Attr('attribute_name').exists()
)
items = response['Items']
for item in items:
    print(item)

# TOTAL COUNT

response = table.scan(
    Select='COUNT'
)
count = response['Count']
print("Total Count:", count)

# PAGINATION
response = table.scan()
items = response['Items']
for item in items:
    print(item)

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    items = response['Items']
    for item in items:
        print(item)

#LIMIT AND OFFSET

response = table.scan(
    Limit=10,
    ExclusiveStartKey={'key_name': 'offset_value'}
)
items = response['Items']
for item in items:
    print(item)

#SORTING(DESC)

response = table.scan(
    ScanIndexForward=False
)
items = response['Items']
for item in items:
    print(item)

#SORTING(ASC)

response = table.scan(
    ScanIndexForward=True
)
items = response['Items']
for item in items:
    print(item)


