def my_user_input_generator(stop_at):
    user_input = ""
    while user_input != stop_at:
        user_input = input("Please enter something: ")
        yield user_input


for user_input in my_user_input_generator('STOP'):
    if user_input != "STOP":
        print(user_input)
