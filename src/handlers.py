from src import provider as PROVIDER


async def do_create_fake_data(field_list, count=1):
    """
    field_list = [
        {"name": "id"},
        {"name": "datetime", "format": "YYYY-MM-DD HH:MM:SS"},
        {"name": "cellphone"},
        {"name": "email"},
        {"name": "price"}
    ]
    """
    datalist = []
    for i in range(count):

        item = {}
        for index, field in enumerate(field_list):
            if field['name'] == 'id':
                value = i + 1
            else:
                func = getattr(PROVIDER, 'generate_' + field['name'])
                value = func(**field)

            item[field['name']] = value

        datalist.append(item)

    return datalist
