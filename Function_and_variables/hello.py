#ask user for their name,remove whitespace and capitalize first letter of each word
name = input("What's your  fullname? ").strip().title()
# Splits user's name
first, last = name.split(" ")
# says hello to user
print(f"hello, {last}")
print(f"hello, {first}")