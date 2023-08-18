def main():
    text = str(input())
    result = convert(text)
    print(result)

def convert(emoji):
    if ":)" in emoji:
        return emoji.replace(":)", "🙂")
    else:
        return emoji.replace(":(", "🙁")

main()