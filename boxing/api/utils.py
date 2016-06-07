import re

import boxing.api.models

def camel_to_snake(name):
    """
    Convert from CamelCase to snake_case, stolen from
    http://stackoverflow.com/questions/1175208/
    elegant-python-function-to-convert-camelcase-to-snake-case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def to_account(account, email_class, **data):
    email_class().send(account.email, **data)

def to_staff(email_class, **data):
    """
    Emails staff, members with is_staff set to True
    """
    staff = boxing.api.models.Account.objects.filter(is_staff=True)
    for account in staff.all():
        email_class().send(account.email, **data)
