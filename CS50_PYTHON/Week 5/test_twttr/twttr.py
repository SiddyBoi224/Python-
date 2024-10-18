def main():
    string = input(str())
    print(shorten(string))


def shorten(string):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for char in string:
        if char not in vowel:
            result += char
    return result


if __name__ == "__main__":
    main()
