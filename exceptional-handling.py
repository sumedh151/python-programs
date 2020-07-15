#implement exception handling

while(1):
    try:
        x=int(input("Enter number 1 : "))
        y=int(input("Enter number 2: "))
        z=x//y
    except ZeroDivisionError as z:
        print("Divide by zero error\r")
    except ValueError as v:
        print("Invalid input\r")
    else:
        print("Float division {}//{} : {}".format(x,y,z))
        break
    finally:
        print("Finally block has been executed")
    
    print()

#raising user defined exception

import random as rand
class Error(Exception):
    # Base class for other exceptions
    pass

class InvalidInputError(Error):
    def __init__(self):
        # Raised when the input value is invalid
        self.message="Invalid Input"

class ValueTooSmallError(Error):
    # Raised when the input value is too small
    def __init__(self):
        self.message="Value greater than guessed"

class ValueTooLargeError(Error):
    # Raised when the input value is too large
    def __init__(self):
        self.message="Value smaller than guessed"

print("\n")
g=rand.randint(1,10)
k=0

while 1:
    k=k+1
    x=int(input("Guess number between 1 to 10 : "))
    try:
        if x<1 or x>10:
            raise InvalidInputError
        else:
            if x<g:
                raise ValueTooSmallError
            elif x>g:
                raise ValueTooLargeError
            else:
                print("Value guessed is correct")
                print("Attempts : ",k)
                break
    except InvalidInputError as i:
        print(i.message)
    except ValueTooSmallError as s:
        print(s.message)
    except ValueTooLargeError as l:
        print(l.message)
    print()
    

