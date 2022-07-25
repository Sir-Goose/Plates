import string


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if length > 6:
        return False
    if length < 2:
        return False
    if s[(length - 2)] == "0":
        return False

    for i in s:
        if i in string.punctuation:
            return False

    return True


main()
