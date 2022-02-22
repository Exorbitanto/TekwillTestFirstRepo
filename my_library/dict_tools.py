def dict_key_with_max_value(my_dict:dict):
    values_list = list(my_dict.values())
    keys_list = list(my_dict.keys())
    return keys_list[values_list.index(max(values_list))] if my_dict else None