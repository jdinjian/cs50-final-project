def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    tip = float(p.replace("%", ""))/100
    return tip


main()



def main():
    text = input()
    textnew = text.replace(" ", "...")
    print(textnew)

main()



def main():
    voice = input()
    indoor_voice = voice.lower()
    print(indoor_voice)

main()

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    text = input()
    newtext = convert(text)
    print(newtext)

main()


def main():
    mass = float(input("m:"))
    joules = int(mass * 90000000000000000)
    print(f"E: {joules}")

main()



