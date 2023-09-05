answer = str(input("What is the Answer to the Great Question of Life, the Universe and Everything? ")).strip().title()

if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")