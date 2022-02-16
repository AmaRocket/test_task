import re

with open("passwords.txt", "r") as data:
    line = data.readlines()


def coun_valid_passwords():
    """
    Reads a file and counts the number of repeated characters in the password.
    If the number matches the range, it adds it to the list.
    :return: Сount of matches in file
    """
    valid_passwords = set()

    for i in line:
        symbols_in_password = str(re.findall(r"^\w", i)[0])
        print("Symbols in password: ", symbols_in_password)

        number_of_times = re.findall(r"(\d)", i)
        start_of_range = int(number_of_times[0])
        end_of_range = int(number_of_times[-1])

        passwords = str((re.findall(r": (\w+)", i))[0])
        print("Must be in range from: ", start_of_range, "to", end_of_range)
        print("Password: ", passwords)

        count_symbols_in_passwords = passwords.count(symbols_in_password)
        print(count_symbols_in_passwords)
        print("+---------------------------+")

        if count_symbols_in_passwords in range(start_of_range, end_of_range + 1):

            valid_passwords.add(passwords)
            print("Password: ", passwords, " - Password is valid")
            print("+---------------------------+")
            print()
        else:
            print("Password: ", passwords, " - Password is not valid")
            print("+---------------------------+")
            print()

    return len(valid_passwords)


print("In this file - ", coun_valid_passwords(), "valid passords")
