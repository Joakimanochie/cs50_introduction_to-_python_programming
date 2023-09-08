import csv

name = input("What's your name? ")
hostel = input("What's your hostel? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "hostel"])
    writer.writerow({"name": name, "hostel": hostel})