import string
if __name__ == "__main__":
    a = reversed(string.ascii_lowercase)
    for i in a:
        print(i)
    print(string.ascii_lowercase)