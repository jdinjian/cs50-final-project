#et cetera
def main():
    n = int(input("Whats n: "))

    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "sheep" * i

if __name__ == "__main__":
    main()

"""
students = ["hermione", "harry", "ron"]

for i, student in enumerate(students):
    print(i + 1, student)


class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow")
args = parser.parse_args()

for _ in range(args.n):
    print("meow")


def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins  = [100,50,25]

print(total(*coins), "Knuts")

** coins if dictionary

* args, **kwargs


def main():
    yell("This", "is", "cs50")


def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

for i in range(len)
"""
