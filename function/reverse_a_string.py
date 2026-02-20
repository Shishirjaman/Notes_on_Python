def reverse_string(string):
    s = string[: :-1]
    return s


if __name__ == "__main__":
    string = input("enter the string: ")
    revstring = reverse_string(string)
    print(revstring)