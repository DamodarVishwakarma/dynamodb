from create_item import table

table.delete_item(
    Key={
        'id': 1,
        'name': 'Test User'
    }
)
