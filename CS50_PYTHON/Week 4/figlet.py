from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

def check():
    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(figlet.getFonts()))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit("Invalid usage")
        else:
            text = input()
            print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")


def main():

    check()

if __name__=="__main__":
    main()
