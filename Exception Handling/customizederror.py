class TooYoung(Exception):
    def __init__(self, arg):
        self.msg=arg

class OldAge(Exception):
    def __init__(self, arg):
        self.msg=arg

age=int(input('Enter age of a person for voting: '))
try:
    if age<18:
        raise TooYoung("Too young to vote...")
    elif age>100:
        raise OldAge("Too old to vote...")
    else: 
        print('Eligible to vote...')
except Exception as msg:
    print(msg)

print("program ended")