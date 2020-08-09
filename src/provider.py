from faker import Faker

FAKE = Faker('zh_CN')


def generate_phone_number(count=1):
    if count > 1:
        return [FAKE.phone_number() for _ in range(count)]
    else:
        return FAKE.phone_number()


def generate_name(gender=None, count=1):
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


def generate_address(count=1):

    if count > 1:
        return [FAKE.address() for _ in range(count)]
    else:
        return FAKE.address()


def generate_email(domain=None, count=1):

    if count > 1:
        return [FAKE.email(domain=domain) for _ in range(count)]
    else:
        return FAKE.email(domain=domain)
