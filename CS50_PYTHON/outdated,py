#date input mm/dd/yyyy
#date output yyyy/mm/dd

def main():
    month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

    while True:
        try:
            date = input("Date: ").strip()
            dateList = spliter(date)
            datecheck = dateCheck(dateList, month)
            if datecheck == 1:
                raise ValueError
            dateOut(dateList, month)
            break
        except ValueError:
            pass
#Code can be split into : data input , Data split, data check, data output

# Split the input into day, month, and year components
def spliter(date):
    ndate = []
    rep = date.replace(",", "").replace("/", " ").replace(" ", "-")
    ndate = rep.split('-')
    return ndate

def dateCheck(dateList, month):
    check = 1
    try:
        if (dateList[0] in month) or (1 <= int(dateList[0]) <= 12):
            if 1 <= int(dateList[1]) <= 31:
                if 1000 <= int(dateList[2]) <= 9999:
                    check = 0
    except (ValueError, IndexError):
        check = 1
    return check

def dateOut(dateList, month):
    if dateList[0] in month:
        dateList[0] = month.index(dateList[0]) + 1
    print(f"{dateList[2]}-{int(dateList[0]):02}-{int(dateList[1]):02}")

main()
