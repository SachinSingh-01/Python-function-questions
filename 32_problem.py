'''Write a function validate_password(password) that:
Returns True if password length ≥ 8
Contains at least one digit
Contains at least one alphabet
Else return False'''
def validate_password(password):
    if len(password)<8:
        return False
    has_digit=False
    has_alpha=False
    for char in password:
        if char.isdigit():
            has_digit=True
        if char.isalpha():
            has_alpha=True
    if has_digit and has_alpha:
        return True
    else:
        return False
result=validate_password("sachin123#")
print(result)