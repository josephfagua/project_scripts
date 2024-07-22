from email_validator import validate_email, EmailNotValidError
import re


def check(emails):
    for email in emails:
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.match(pat, email):
            print("Valid Email " + email)
        else:
            print("Invalid Email " + email)


def email_validator(emails):
    for email in emails:
        try:
            validate = validate_email(email)

            print("Email: " + email + " is a valid email address")
        except EmailNotValidError as e:
            print(str(e))


def validate_email(your_pattern, emails):
    pattern = re.compile(your_pattern)
    # here is an example list of email to check it at the end

    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % email)
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


def main():
    email_list = {"fagua.danel@hotmail.com", "stellaag_70@hotmail.com",
                  "joseph05fagua@gmail.co.uk", "Raulp1@yahoo.com", "JAguilar1673@outlook.com", "foo@bar@google.com"}
    # email_validator(email_list)
    pattern = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$"
    validate_email(pattern, email_list)
    # check(email_list)


if __name__ == '__main__':
    main()
