import random

def choice():
    while True:
        try:
            x = int(input("Level: "))
        except ValueError:
            pass
        else:
            return x

def check(x):
    while True:
        try:
            num = random.randint(1,x)
            while True:
                guess = int(input("Guess: "))
                if(guess>num):
                    print("Too large!")
                elif(guess<num):
                    print("Too small!")
                elif(guess==num):
                    print("Just right!")
                    raise EOFError
        except ValueError:
            pass
        except EOFError:
            break

def main():
    x = choice()
    check(x)
    
if __name__=="__main__":
    main()
