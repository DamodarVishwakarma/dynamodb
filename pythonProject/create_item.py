import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

item = {
    'id': 14,
    'name': 'pink',
    'role_id': 4,
    'email': 'pink@gmail.com',
    'password': 'pink123',
    'created_by': 1,
    'created_on': 1631744876,
    'status': 'active'
}

table.put_item(Item=item)
