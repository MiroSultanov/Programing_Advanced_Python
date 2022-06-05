from custom_exeption import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

def email_validator(input_email):

    email_parts = input_email.split('@')

    if len(email_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    email_name, server_name = email_parts

    if len(email_name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    domain = f'.{server_name.split(".")[-1]}'

    if domain not in valid_domains:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')


    print("Email is valid")

valid_domains = {'.com', '.bg', '.org', '.net'}
input_email = input()
email_validator(input_email)

