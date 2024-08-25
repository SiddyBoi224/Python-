def main():
    grocery={}
    while True:
        try:
            veg = input()
            if veg in grocery:
                grocery[veg] += 1
            else:
                grocery[veg] = 1
        except (ValueError, KeyError):
            pass
        except EOFError:
            sorted(grocery)
            for key, value in sorted(grocery.items()):
                print(f"{value} {key.upper()}")
            break

main()
