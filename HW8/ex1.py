user_input = input("Introduceti o valoare si vazic ce fel de tip este: ")

try:
    int(user_input)
    print("You have entered an integer.")
except ValueError:
    try:
        float(user_input)
        print("You have entered a float.")
    except ValueError:
        print("You have entered a string.")

