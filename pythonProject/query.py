import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

# SORTING
# response = table.query(
#     ScanIndexForward=False,  # for descending order
#     KeyConditionExpression=Key('id').eq(5)
# )
# print(response['Items'])


# Set the desired page size
# PAGINATION
# page_size = 10
#
# start_key = None
#
# while True:
#     if start_key:
#         response = table.scan(
#             ExclusiveStartKey=start_key,
#             Limit=page_size
#         )
#     else:
#         response = table.scan(Limit=page_size)
#
#     items = response['Items']
#     print(len(items))
#     for item in items:
#         print(item)
#
#     if 'LastEvaluatedKey' in response:
#         start_key = response['LastEvaluatedKey']
#     else:
#         break

# LIMIT AND OFFSET

# limit = 10  # Number of items per page
# offset = 20  # Number of items to skip from the start
#
# # Calculate the number of pages and start key
# pages = offset // limit
# start_key = None
#
# for _ in range(pages):
#     response = table.scan(Limit=limit, ExclusiveStartKey=start_key)
#     start_key = response.get('LastEvaluatedKey')
#
# # Fetch the desired page
# params = {'Limit': limit}
# if start_key:
#     params['ExclusiveStartKey'] = start_key
#
# response = table.scan(**params)
#
# items = response['Items']
# for item in items:
#     # Process each item as needed
#     print(item)

# limit = 10
# offset = 20
# pages = offset // limit
#
# start_key = None
#
# while True:
#     if start_key:
#         response = table.scan(
#             ExclusiveStartKey=start_key,
#             Limit=pages
#         )
#     else:
#         response = table.scan(Limit=pages)
#
#     items = response['Items']
#     for item in items:
#         print(item)
#
#     if 'LastEvaluatedKey' in response:
#         start_key = response['LastEvaluatedKey']
#     else:
#         break

# SORTING WITH MISSING OR NULL VALUES

# response = table.query(
#     # IndexName='YourIndexName',
#     KeyConditionExpression=Key('id').eq(5),
#     ScanIndexForward=True,
#     ExpressionAttributeNames={
#         '#sortKey': 'email'
#     },
#     ExpressionAttributeValues={
#         ':nullValue': None
#     },
#     FilterExpression='attribute_not_exists(#sortKey) OR #sortKey = :nullValue',
#     ProjectionExpression='id',
#     ConsistentRead=True
# )
#
# items = response['Items']
# for item in items:
#     # Process each item as needed
#     print(item)

# EXACT MATCH

# response = table.query(
#     KeyConditionExpression=Key('id').eq(5)
# )
# items = response['Items']
# for item in items:
#     print(item)

# OVERLAP

# response = table.scan(
#     FilterExpression=Attr('email').contains('damodar')
# )
# items = response['Items']
# for item in items:
#     print(item)

# ILIKE

#  similar to contains or overlap

# OVERLAP WITH []
# values_to_check = ['max@gmail.com', 'test@gmail.com']
#
# response = table.scan(
#     FilterExpression=Attr('email').is_in(values_to_check)
# )
# items = response['Items']
# for item in items:
#     print(item)
