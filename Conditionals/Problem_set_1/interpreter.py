def main():
    user_input = input("Expression: ")
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Please enter an expression in the format 'x operator y'")
    else:
        try:
            x = int(parts[0])
            operator = parts[1]
            y = int(parts[2])
            
            result = calculate_expression(x, operator, y)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {result:.1f}")
        except ValueError:
            print("Invalid input. Please enter valid integers for x and z.")



def calculate_expression(x, operator, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        if y == 0:
            return "Error: Division by zero"
        return x / y
    else:
        return "Error: Invalid operator"


if __name__ == "__main__":
    main()