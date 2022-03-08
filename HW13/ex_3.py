def printer_decorator(funct):
    # Processing args for our function
    def wrapper_function(*args, **kwargs):
        # Passing arguments back to our function.
        arg_list = args[0]
        for arg in arg_list:
            if type(arg) == int or type(arg) == float:
                pass
            else:
                raise TypeError

        value_returned = funct(*args, **kwargs)
        print(value_returned)
        return value_returned


    return wrapper_function

@printer_decorator
def list_sum(list_of_elements):
    return sum(list_of_elements)

list_sum([4,849,"62",5])