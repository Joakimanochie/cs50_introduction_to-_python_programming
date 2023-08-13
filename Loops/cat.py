def main():
    number = get_num()
    meow(number)

def get_num():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(x):
    for _ in range(x):
        print("meow")

main()
