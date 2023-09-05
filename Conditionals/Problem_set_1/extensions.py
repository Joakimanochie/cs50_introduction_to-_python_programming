def main():
    exe = input("File name: ")
    print_exe(exe)

def print_exe(file):
    if file.endswith(".jpeg") == True:
        print("image/jpeg")
    elif file.endswith(".jpg") == True:
        print("image/jpeg")
    elif file.endswith(".gif") == True:
        print("image/gif")
    elif file.endswith(".png") == True:
        print("image/png")
    elif file.endswith(".pdf") == True:
        print("application/pdf")
    elif file.endswith(".txt") == True:
        print("text/plain")
    elif file.endswith(".zip") == True:
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()