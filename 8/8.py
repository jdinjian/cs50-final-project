class Wizard:
     def __init__(self, name):
        if not name:
            raise ValueError("missing name")
        self.name = name

class Professor(Wizard):
     def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

object.__add__(self, other)




#seasons

from datetime import date
import inflect
engine = inflect.engine()
import sys
import re

class AgeCalculator:
    def __init__(self, birth_str):
        self.birth_str = birth_str
        self.birth = None
        self.age_min = None

    def validate(self):
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(pattern, self.birth_str):
            return False
        return True

    def date_check(self):
        try:
            year, month, day = map(int, self.birth_str.split('-'))
            self.birth = date(year, month, day)
            return True
        except ValueError:
            return False

    def calculate_age(self):
        today = date.today()
        lifetime = (today - self.birth).days
        self.age_min = lifetime * 24 * 60
        return self.age_min

    def number_to_word(self):
        return engine.number_to_words(self.age_min, andword='')

    def run(self):
        if not self.validate():
            sys.exit("Invalid Date")
        if not self.date_check():
            sys.exit("Invalid Date")
        age_min = self.calculate_age()
        print(self.number_to_word().capitalize(), "minutes")



def main():
    inpu = input("Date of Birth: ")
    calculator = AgeCalculator(inpu)
    calculator.run()


if __name__ == "__main__":
    main()

#test_seasons

import seasons

def test_validate():
    age_valid = seasons.AgeCalculator("2000-01-01")
    age_invalidf = seasons.AgeCalculator("2000/01/01")
    age_invalidd = seasons.AgeCalculator("2000-02-35")

    assert age_valid.validate() == True
    assert age_valid.date_check() == True
    assert age_invalidf.validate() == False
    assert age_invalidf.date_check() == False
    assert age_invalidd.date_check() == False


#Jar

class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._cookie = 0
        if capacity < 0:
            raise ValueError("Capacity cannot negative")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookie

    def deposit(self, n):
        if n < 0:
            raise ValueError("negative cookies")
        if self._cookie + n > self._capacity:
            raise ValueError("Exceeds Capacity")
        self._cookie += n


    def withdraw(self, n):
        if n <0:
            raise ValueError("Cant deposit negative cookies")
        if self._cookie - n < 0:
            raise ValueError("Negative capacity")
        self._cookie -= n

    def __str__(self):
        return ("🍪" * self._cookie)

#test_jar

from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(4)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(14)
def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9

#cs50_shirtificate

from fpdf import FPDF
from PIL import Image

name = input("Name: ") + (" took CS50")
pdf = FPDF(format = 'A4')
pdf.add_page()
Image.open("shirtificate.png")
pdf.set_font("Arial", size = 28)
pdf.image("shirtificate.png", x= 5, y= 65, w =200)
pdf.set_text_color(255,255,255)
pdf.header
pdf.cell(0, 250 , name, ln=True, align = 'C')

pdf.set_font("Arial", size = 50)
pdf.set_text_color(0,0,0)
pdf.cell(0, -450, "CS50 Shirtificate", ln =True, align="C")

pdf.output("shirtificate.pdf")


