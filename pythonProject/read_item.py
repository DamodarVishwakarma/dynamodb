from create_item import table

response = table.get_item(
    Key={
        'id': 5,
        'name': 'Test'
    }
)

# Access the retrieved item
item = response['Item']
print(item)
