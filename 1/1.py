# BANK
 

# DEEP
answer = input("What is the Answer to the Great Question of Life, the Universe and Everything?").lower().replace(" ", "")

match answer:
    case "42" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")

# EXTENSIONS
answer = input('File.name:').lower().replace(" ", "")

if answer.endswith('.gif'):
    print ('image/gif')
elif answer.endswith('.jpg') or answer.endswith('.jpeg'):
    print ('image/jpeg')
elif answer.endswith('.png'):
    print ('image/png')
elif answer.endswith('.pdf'):
    print ('application/pdf')
elif answer.endswith('.txt'):
    print ('text/plain')
elif answer.endswith('.zip'):
    print ('application/zip')
else:
    print('application/octet-stream')

#INTERPRETER
def main():
    answer = input("Expression:")
    x, y, z = answer.split(" ")
    x, z = float(x), float(z)
    match y:
        case "*": return x * z
        case "/": return x / z
        case "+": return x + z
        case "-": return x - z
print(main())

#MEAL
def main():
    time = input("What time is it?:")
    a, b = time.split(":")
    a, b = int(a), int(b)
    if a == 7 or a == 8 and b == 0:
        print("breakfast time")
    elif a == 12 or a == 13 and b == 0:
        print("lunch time")
    elif a == 18 or a == 19 and b == 0:
        print("dinner time")

def convert(time):
    c, d = time.split(":")
    c, d = float(c), float(d)
    d = d/60
    return(c + d)

if __name__ == "__main__":
    main()


