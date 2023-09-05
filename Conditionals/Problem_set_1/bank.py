bank_statement = input("Greetings: ").strip().title()

match bank_statement:
    case "Hello" | "Hello, Newman":
        print("$0")
    case "How you doing?" | "Hey?" | "How's it going?":
        print("$20")
    case "What's happening?" | "What's up":
        print("$100")