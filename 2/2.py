#twttr
word = input("Input: ")
output = ""
for c in word:
    if c not in ["O", "o", "E", "e", "I", "i", "U", "u", "A", "a"]:
        output += c

print(output)

#plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
   if len(p) < 2 or len(p) > 6:
       return False
   for c in p:
       if not c.isalnum():
          return False
   if p[0].isdigit() or p[1].isdigit():
       return False
   numStart = None
   for a in range(len(p)):
       c = p[a]
       if c.isdigit():
           numStart = a
           break
   if numStart is None:
        return True
   if p[numStart] == '0' :
       return False
   for a in range(numStart, len(p)):
       if not p[a].isdigit():
           return False
   else:
       return True

main()

#nutrition
item = input("Item: ").lower().replace(" ", "")
fruits = [
    {"fruit" : "apple", "calories" : "130"},
    {"fruit" : "avocado", "calories" : "50"},
    {"fruit" : "banana", "calories" : "110"},
    {"fruit" : "cantaloupe", "calories" : "50"},
    {"fruit" : "grapefruit", "calories" : "60"},
    {"fruit" : "grapes", "calories" : "90"},
    {"fruit" : "honeydewmelon", "calories" : "50"},
    {"fruit" : "kiwifruit", "calories" : "90"},
    {"fruit" : "lemon", "calories" : "15"},
    {"fruit" : "lime", "calories" : "20"},
    {"fruit" : "nectarine", "calories" : "60"},
    {"fruit" : "orange", "calories" : "80"},
    {"fruit" : "peach", "calories" : "60"},
    {"fruit" : "pear", "calories" : "100"},
    {"fruit" : "pineapple", "calories" : "50"},
    {"fruit" : "plums", "calories" : "70"},
    {"fruit" : "strawberries", "calories" : "50"},
    {"fruit" : "sweetcherries", "calories" : "100"},
    {"fruit" : "tangerine", "calories" : "50"},
    {"fruit" : "watermelon", "calories" : "80"}
    ]
for fruit in fruits:
    if fruit["fruit"] == item:
        print(f"Calories: {fruit['calories']}")

#coke
amount = 50
while amount > 0:
   print("Amount Due:", amount)
   coin = int(input("Insert Coin: "))
   if coin in [25, 10, 5]:
        amount -= coin
   else:
        continue
if amount <= 0:
    change = -amount
    print("Change Owed:", change)

#CAMEL
answer = input("camelCase: ")
snake_case = ""
for letter in answer:
    if letter.isupper():
        snake_case += "_" + letter.lower()
    else:
        snake_case += letter
print(snake_case)
