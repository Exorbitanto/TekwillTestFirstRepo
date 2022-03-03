class NumberList(list):

    def __init__(self, list_of_values=None):
        self._verify_is_float_only(list_of_values)
        super().__init__(list_of_values)

    def __str__(self):
        return super().__str__()

    def get_sum(self):
        sum = 0
        for element in self:
            sum += float(element)
        return sum

    def get_average(self):
        sum = self.get_sum()
        average = sum / len(self)
        return average

    def append(self, new_value):
        if self._verify_is_float_only([new_value]):
            super().append(new_value)

    def extend(self, list_of_new_values):
        self._verify_is_float_only(list_of_new_values)
        super().extend(list_of_new_values)

    def _verify_is_float_only(self, list_to_verify):
        for i in list_to_verify:
            try:
                float(i)
                return True
            except ValueError("There is one or more string value's than cannot be converted to a float, please try again."):
                return False
