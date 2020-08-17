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



async def create_data_sql(field_list, value_list):
    """Create sql string.

    :params field_list: ['id', 'name', 'datetime']
    :params value_list: [("1", "名称", "2020-05-01"), ("2", "名称2", "2020-06-01")]
    """
    tpl = """INSERT INTO `table_name`\n\t{fields}\nVALUES\n\t{value_list};"""

    fields_str = '({})'.format(', '.join(field_list))

    value_str_list = []
    for item in value_list:
        item_list = ['"{}"'.format(i) for i in item]
        value_str_list.append('({})'.format(', '.join(item_list)))

    value_list_str = ', \n\t'.join(value_str_list)

    result = tpl.format(fields=fields_str, value_list=value_list_str)

    return result
