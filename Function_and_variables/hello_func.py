def main():
   name = input("What's your  fullname? ").strip().title()
   hello(name) 


def hello(to="world"):
    print("hello,", to )


main()