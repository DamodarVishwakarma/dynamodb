from create_item import table

table.update_item(
    Key={
        'id': 1,
        'name': 'Damodar'
    },
    UpdateExpression='SET email = :email',
    ExpressionAttributeValues={
        ':email': 'test.email@example.com'
    }
)
print("Item updated successfully")
response = table.scan()
items = response['Items']
for item in items:
    print(item)
