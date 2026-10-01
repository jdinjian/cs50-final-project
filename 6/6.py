
#lines
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    program = sys.argv[1]
    if not program.endswith('.py'):
        sys.exit("Not a python file")
    else:
        try:
            count = 0
            with open(sys.argv[1], "r") as file:
                for line in file:
                    if line.strip():
                        row = line.strip()
                        if not row[0] == "#":
                            count += 1
                        else:
                            continue
            print(count)
        except FileNotFoundError:
            sys.exit("File does not exist")

#pizza
from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    program = sys.argv[1]
    if not program.endswith('.csv'):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.reader(file)
                header = next(reader, None)
                data = []
                for row in reader:
                    data.append(row)
                print(tabulate(data, headers = header, tablefmt="grid", stralign="left"))
        except FileNotFoundError:
            sys.exit("File does not exist")

#scourgify
import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    program1, program2 = sys.argv[1], sys.argv[2]
    students = []
    try:
        with open(program1, "r", newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                name, house = row[0], row[1]
                last, first = name.split(",", 1)
                last, first = last.strip(), first.strip()
                students.append({"first": first,"last": last, "house": house})
            with open(program2, mode="w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                writer.writerows(students)



    except FileNotFoundError:
            sys.exit("error")

#shirt
import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    before1, after2 = sys.argv[1], sys.argv[2]
    try:
        before, beforeend = os.path.splitext(before1)
        after, afterend = os.path.splitext(after2)
        if beforeend == afterend:
            if not before1.endswith(".jpg") or before1.endswith(".jpeg") or before1.endswith(".png"):
                sys.exit("Invalid input")
            else:
                before2 = Image.open(before1)
                before3 = ImageOps.fit(before2, (600, 600))
                shirt1 = Image.open("shirt.png")
                shirt2 = ImageOps.fit(shirt1, (300,300))
                before3.paste(shirt1, shirt1)
                before3.save(after2)
        else:
            sys.exit("Input and output have different extensions")

    except ValueError:
        sys.exit("error1")

