def age_seconds():

    user_age = input("Enter your age: ")
    seconds = int(user_age) * 365 * 24 * 60 * 60
    print("Your age in seconds is {}: ".format(seconds))

age_seconds()