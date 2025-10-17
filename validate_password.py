# Question 1
import string
def validate_password(password: str) -> bool:
    """
    STEP 1: Create a function that validates a password based on the following rules:
        - It must be at least 8 characters long.
        - It must contain at least one uppercase letter.
        - It must contain at least one lowercase letter.
        - It must contain at least one digit.
        - It must contain at least one special character (e.g. @, #, $, %, !).

    TODO: Implement logic to check all these conditions and return True if valid, otherwise False.
    """

    if type(password) is not str:
        raise TypeError("Enter a string")
    if not password:
        raise ValueError("No input")
    

    small=False
    big=False
    big=False
    dig=False
    spe=False
    long=False
    for letter in password:
        if letter.islower():
            small=True
        if letter.isupper():
            big=True
        if letter.isdigit():
            dig=True
        if letter in string.punctuation:
            spe=True

    if len(password)>=8:
        long=True
    
    if small==True and big==True and dig==True and spe==True and long==True:
        result=True
    else:
        result=False


    return result



# Question 2
def password_strength(password: str) -> str:
    """
    STEP 2: Determine the strength of a given password and return it as a string.

    Criteria:
        - "Weak" if the password is less than 8 characters long.
        - "Moderate" if it has 8 or more characters but is missing one or more
          of the following: uppercase, lowercase, digit, or special character.
        - "Strong" if it meets all password validation rules from Question 1.

    TODO: Implement the function to return one of these three strings.
    """
    if not password:
        raise ValueError("No input")
    
    if type(password) is not str:
        raise TypeError("Enter a String")
    
    if len(password)<8:
        return "Weak"

    if validate_password(password)==True:
        return "Strong"
    
    if len(password)>=8 and validate_password(password)==False:
        return "Moderate"
    
    
    
    
    return ""

print(password_strength("Password"))

