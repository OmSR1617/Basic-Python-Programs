import string

password = input("Enter Your Password: ")

def strong():
    if (len(password) >= 8 and
        any(ch in string.ascii_uppercase for ch in password) and
        any(ch in string.ascii_lowercase for ch in password) and
        any(ch in string.digits for ch in password) and
        any(ch in "!£$%&+_-@/?" for ch in password)):
        return "Your Password is Strong"

def medium():
    if (len(password) <= 8 and
        any(ch in string.ascii_uppercase for ch in password) and
        any(ch in string.ascii_lowercase for ch in password) and
        any(ch in string.digits for ch in password)):
        return "Your Password is Medium"

def weak():
    if len(password) < 8:
        return "Your Password is Weak"

strongpass = strong()
medpass = medium()
weakpass = weak()

if strongpass:
    print(strongpass)
elif medpass:
    print(medpass)
elif weakpass:
    print(weakpass)
else:
    print("Your Password is Weak")