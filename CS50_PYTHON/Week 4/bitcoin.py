import requests
import sys
import json

def rate(num):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #print(json.dumps(response.json(), indent = 4))
        response = response.json()
        price = float(response["bpi"]["USD"]["rate_float"])
        n_price = price * num
        print(f"${n_price:,.4f}")
    except requests.RequestException:
        print(response.status_code)


def main():

    if len(sys.argv) == 2:
        try:
            rate(float(sys.argv[1]))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


if __name__=="__main__":
    main()
