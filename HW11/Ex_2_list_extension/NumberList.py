class NumberList(list):

    def __init__(self, list_of_values: list):
        for element in list_of_values:
            self._verify_is_float(element)
        self.list_of_values = list_of_values

    def __str__(self):
        return str(self.list_of_values)

    def get_sum(self):
        sum = 0
        for element in self.list_of_values:
            sum += float(element)
        return sum

    def get_average(self):
        sum = self.get_sum()
        average = sum / len(self.list_of_values)
        return average

    def append(self, new_value):
        if self._verify_is_float(new_value):
            self.list_of_values.append(new_value)

    def extend(self, list_of_new_values):
        for element in list_of_new_values:
            self._verify_is_float(element)
        self.list_of_values.extend(list_of_new_values)

    def _verify_is_float(self, value):
        try:
            float(value)
            return True
        except ValueError("There is one or more string value's than cannot be converted to a float, please try again."):
            return False


