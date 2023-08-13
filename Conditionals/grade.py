score = int(input("Score: "))

if score >= 70 and score <= 100:
    print("Grade: A")
elif score >=60 and score < 69:
    print("Grade: B")
elif score >=50 and score < 59:
    print("Grade: C")
elif score >=40 and score < 49:
    print("Grade: E")
else:
    print("Grade: F")