import inflect

p=inflect.engine()

def names():
    list = []
    while True:
        try:
            name = input("Name: ").strip().title()
            list.append(name)
        except EOFError:
            print("Adieu, adieu, to", p.join(list))
            break

def main():
    names()

if __name__=="__main__":
    main()
