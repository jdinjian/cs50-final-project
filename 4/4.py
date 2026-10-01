import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

    #sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
   ## print("Too many arguments")
#else:
    ##print("hello, my name is", sys.argv[1])

#emojize
import emoji

inp = input("Input: ")
result = emoji.emojize(inp, language = 'alias')
print(result)

#figlet
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
font = random.choice(fonts)

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
       fontname = sys.argv[2]
       try:
          fig = Figlet(font = fontname)
       except FontNotFound:
          sys.exit["Invalid usage"]
       inp = input("Input: ")
       print(fig.renderText(inp))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    inp = (input("Input: "))
    fig = Figlet(font = font)
    print(fig.renderText(inp))
else:
    sys.exit("Invalid usage")

#adieu
import inflect
p = inflect.engine()
lister = []
try:
    while True:
        inp = input("Name: ")
        lister.append(inp)
except EOFError:
    print("/n")
    pri = p.join(lister)
    print(f"Adieu, adieu, to {pri}")

#game
import random
import sys
while True:
    try:
        inp = int(input("Level: "))
        numb = random.randint(1, inp)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess > 0:
                    if guess > numb:
                        print("Too large!")
                    elif guess < numb:
                        print("Too small!")
                    elif guess == numb:
                        print("Just right!")
                        sys.exit()
                else:
                    continue
            except ValueError:
                continue
    except ValueError:
        continue

#professor
import random
import sys

def main():
    count = 0
    correct = 0
    level = get_level()
    while True:
        if count < 10:
            x, y = int(generate_integer(level)), int(generate_integer(level))
            z = x + y
            count2 = 0
            while count2 < 3:
                answer = int(input(f"{x} + {y} = "))
                if count2 < 2:
                    if answer == z:
                        count += 1
                        correct += 1
                        break
                    elif answer != z:
                        print("EEE")
                        count2 += 1
                        continue
                    else:
                        print("else")
                elif count2 == 2:
                    print("EEE")
                    print(f"{x} + {y} = {z}")
                    count += 1
                    break
        if count == 10:
            print(f"Score: {correct}")
            break

def get_level():
    while True:
        try:
            level = input("Level: ")
            lev = int(level)
            if lev not in (1,2,3):
                raise ValueError
            else:
                return lev
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        digit = random.randint(0, 9)
        return digit
    elif level == 2:
        digit = random.randint(10, 99)
        return digit
    elif level == 3:
        digit = random.randint(100, 999)
        return digit

if __name__ == "__main__":
    main()

#bitcoin
import requests
import sys
try:
    if len(sys.argv) == 2:
        try:
            inte = float(sys.argv[1])
            if inte >= 0:
                req = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=60d87bcc0a5ea02b3b22ad251635eabeb9d3e2936173369236fe3327a8d83bce")
                req.raise_for_status()
                jjson = req.json()
                answer = jjson.get('data',{}).get('priceUsd')
                answer2 = float(answer) * inte
                print(f"${answer2:,.4f}")
            else:
                print("invalid amount")
        except ValueError:
            sys.exit("Command-line argument is not a number")
            
    elif len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        sys.exit()

except requests.RequestException:
    print("except")
