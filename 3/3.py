#fuel
while True:
    try:
        fraction = input("Fraction:")
        x1, y1 = fraction.split("/")
        x, y = float(x1), float(y1)
    except (ValueError, ZeroDivisionError):
        continue

    if x < 0 or y <= 0:
        continue
    if y != int(y) or x != int(x):
        continue

    value = round((x/y) * 100)

    if value > 100:
        continue
    elif value < 0:
        continue
    elif value >= 99:
        print("F")
    elif value <= 1:
        print("E")
    else:
        print(f"{value}%")
    break

#taqueria
total = 0
menu = {
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
try:
    while True:
        order = input("Item: ").title()
        for item, cost in menu.items():
            if order == item:
                total += float(cost)
                print(f"${total:.2f}")
except EOFError:
    print("")

#grocery
shop_count = {}
try:
    while True:
        item = input("").upper()

        if item in shop_count:
            shop_count[item] += 1
            shop_count
        else:
            shop_count[item] = 1


except EOFError:
    sorted_items = sorted(shop_count.keys())
    for item in sorted_items:
        count = shop_count[item]
        print(f"{count} {item}")

#outdated
months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}
while True:
    answer = input("Date: ")
    if "/" in answer:
        parts = answer.split("/")
        if len(parts) == 3:
            month_str, day_str, year_str = parts
            try:
                month = int(month_str)
                day = int(day_str)
                year = int(year_str)
                if 1 <= month <= 12 and 1<= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            except ValueError:
                continue
    elif " " in answer:
        if "," in answer:
            parts = answer.split(" ")
            if len(parts) == 3:
                month_name, day_part, year_part = parts
                month_name = month_name.capitalize()
                day = day_part.replace(",", "")
                month_num = months.get(month_name)
                if month_num:
                    if month_num is not None:
                        day = int(day)
                        year = int(year_part)
                        month = int(month_num)
                        try:
                            if 1<= day <= 31:
                                print(f"{year}-{month:02}-{day:02}")
                                break
                        except (NameError, ValueError):
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
