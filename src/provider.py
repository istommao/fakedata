import datetime

from faker import Faker

FAKE = Faker('zh_CN')


def generate_cellphone(count=1, **kwargs):
    if count > 1:
        return [FAKE.phone_number() for _ in range(count)]
    else:
        return FAKE.phone_number()


def generate_name(gender=None, count=1, **kwargs):
    if gender == 'male':
        func = FAKE.name_male
    elif gender == 'female':
        func = FAKE.name_female
    else:
        func = FAKE.name

    if count > 1:
        return [func() for i_ in range(count)]
    else:
        return func()


def generate_address(count=1, **kwargs):

    if count > 1:
        return [FAKE.address() for _ in range(count)]
    else:
        return FAKE.address()


def generate_email(domain=None, count=1, **kwargs):

    if count > 1:
        return [FAKE.email(domain=domain) for _ in range(count)]
    else:
        return FAKE.email(domain=domain)


def generate_number_str(digits=1, decimal=0, count=1, **kwargs):
    text = '%' + '#' * (digits - 1)

    if decimal > 0:
        text = '{}.{}'.format(text, '#' * decimal)

    if count > 1:
        return [FAKE.numerify(text=text) for _ in range(count)]
    else:
        return FAKE.numerify(text=text)


def generate_datetime(count=1, **kwargs):
    result = FAKE.date_time_between(start_date='-2M')
    return str(result)


def generate_price(digits=1, decimal=0, count=1, **kwargs):
    result = generate_number_str(digits=digits, decimal=decimal, count=count)
    if '.' in result:
        return float(result)
    else:
        return int(result)


def generate_number(digits=1, decimal=0, count=1, **kwargs):
    result =  generate_number_str(digits=digits, decimal=decimal, count=count)
    if '.' in result:
        return float(result)
    else:
        return int(result)
