def main():
    print("Welcome")
    while True:
        age = int(input("How Old Are You?"))
        has_id = int(input("Do You Have ID?"))
        # age=18
        # has_id = True
        should_pour_drink = should_pour(age, has_id)
        print(age)
        print(has_id)
        print(should_pour_drink)

        print_message(should_pour_drink)
        # pour(age, has_id)


# def pour(age, has_id):
#     """Decide if we should pour a drink. Are they underage?"""
#     if (age >= 21) and (has_id == True):
#         print("Serve Them A Drink")
#     else:
#         print("You Need to Leave")


def should_pour(age, has_id):
    if (age >= 21) and (has_id == True):
        return True
    return False


def print_message(should_pour_drink):
    if should_pour_drink:
        print("Serve Them A Drink")
    print("You Need to Leave")


if __name__ == "__main__":
    main()
