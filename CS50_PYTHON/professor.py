import random

def get_level():
    while True:
        try:
            x = int(input("Level: "))
        except ValueError:
            pass
        else:
            if x == 1 or x == 2 or x == 3:
                return x
            else:
                pass


def generate_integer(level):
    if level == 1:
        a = random.randint(0,9)
        b = random.randint(0,9)
    elif level == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
    elif level == 3:
        a = random.randint(100,999)
        b = random.randint(100,999)
    return a,b


def main():
    score = 0
    error = 0
    lv = get_level()
    for _ in range(10):
        x,y = generate_integer(lv)
        while True:
            try:
                if error == 3:
                    print(f"{x} + {y} = {x+y}")
                    error = 0
                    break
                else:
                    print(f"{x} + {y} = ", end="")
                ans = int(input())
                if ans == x+y:
                    score += 1
                    error = 0
                    break
                else:
                    raise ValueError
            except ValueError:
                error += 1
                print("EEE")
                pass

    print("Score:", score)


if __name__=="__main__":
    main()
