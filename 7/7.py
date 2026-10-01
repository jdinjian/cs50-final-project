import re

email = input("What your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

url.removeprefix(")

#numb3rs
import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
    if re.match(pattern, ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()



from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") is True
    assert validate("30.256.5000.30") is False
    assert validate("30.30.30.30.30") is False

def test_validate2():
    assert validate("255.255.255") is False
    assert validate("30.256.30.30") is False
    assert validate("256.30.30.30") is False

#watch
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if crc := re.search(r"<iframe[^>]*src=\"([^\"]+).*", s):
        url = crc.group(1)
        if ending := re.search(r"^https?://(?:www\.)?youtube\.com/embed/(.+)$", url):
            ending2 = ending.group(1)
            final = f"https://youtu.be/{ending2}"
            return final
        else:
            return("None")
    else:
        return("None")


if __name__ == "__main__":
    main()


#working
import re
import sys


def main():
    print(convert(input("Hours: ")))

checktime = r"^(([0-9]|1[0-2])(?::([0-5][0-9])?)? (AM|PM) to ([0-9]|1[0-2])(?::([0-5][0-9])?)? (AM|PM)$)"
def convert(s):
    if times := re.search(checktime, s):
        first, first2, med1, second, second2, med2 = times.group(2), times.group(3), times.group(4), times.group(5), times.group(6), times.group(7)
        first, second = int(first), int(second)
        if med1 == "PM" and first != 12:
            first = first + 12
        if med2 == "PM" and second != 12:
            second = second + 12
        if first == 12 and med1 == "AM":
            first = first -12
        if second == 12 and med2 == "AM":
            second = second -12
        if not first2 or not second2:
            if first2:
                second2 = "00"
            elif second2:
                first2 = "00"
            else:
                first2, second2 = "00", "00"

        return (f"{first:02d}:{first2} to {second:02d}:{second2}")

    else:
        raise ValueError


if __name__ == "__main__":
    main()


from working import convert
import pytest

def test_errors():
    with pytest.raises(ValueError):
        convert("6 AM to 4:30")
    with pytest.raises(ValueError):
            convert("6 to 4:30 PM")
    with pytest.raises(ValueError):
            convert("6:15 AM - 4:30 PM")
    with pytest.raises(ValueError):
            convert("6:15 AM to 13:00 PM")

def test_convert():
    assert convert("6:30 AM to 5 PM") == "06:30 to 17:00"
    assert convert("8:00 PM to 4:00 AM") == "20:00 to 04:00"


def test_midnight():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

#um
import re
import sys


def main():
    print(count(input("Text: ")))



def count(s):
    uhms = re.findall(r'(?=(\bum\b))', s, re.IGNORECASE)
    uhhms = len(uhms)
    return uhhms


if __name__ == "__main__":
    main()

from um import count

def test_um():
    assert count("um um um") == 3
    assert count("um, in my um mm umm") == 2

def test_uhm():
    assert count("tummy yummy bummy um") == 1
    assert count("yabadabo do um") == 1

def test_uhhm():
    assert count("um, um! um? umm um.") == 4
    assert count("uM, Um! UM? umm um.") == 4


#response
from validator_collection import validators

try:
    email_address = validators.email(input("What's your email address? "))
    print("Valid")
except ValueError:
    print("Invalid")

