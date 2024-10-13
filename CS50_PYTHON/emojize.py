import emoji

def main():
    while True:
        x = input()
        print(emoji.emojize(x , language='alias'))
        exit()


if __name__=="__main__":
    main()
