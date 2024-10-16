def main():
    Bill = 0
    while True:
        try:
            order = input("Item: ")
            Bill += OrderProcess(order.title())
            print(f"Total: ${Bill:.2f}")

        except ValueError:
            pass
        except EOFError:
            break

def OrderProcess(order):
    Menu: dict[str, float] = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    if order in Menu:
        Bill = Menu.get(order)
        return Bill
    else:
        return 0



main()
