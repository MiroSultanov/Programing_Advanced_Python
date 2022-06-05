# You will be given some emails until you receive the command "End". Create the following custom exceptions to validate the emails:
# •	NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the email "peter@gmail.com")
# •	MustContainAtSymbolError - raise it when there is no "@" in the email
# •	InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
# When an error is encountered, raise it with an appropriate message:
# •	NameTooShortError - "Name must be more than 4 characters"
# •	MustContainAtSymbolError - "Email must contain @"
# •	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
# Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
# If the current email is valid, print "Email is valid" and read the next one


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

