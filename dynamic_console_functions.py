
#The function for user input, you send through the list of options that can be selected and then the query string and it returns the index in the option list.
def user_input(_option_list:list, _input_text:str = "What would you like to do? ", _display_options = False) -> int:
    if _display_options:
        for option in _option_list:
            print(option)
    valid = False
    while not valid:
        user_input = input(_input_text)
        if user_input in _option_list:
            option = _option_list.index(user_input)
            valid = True
            return option
        else:
            try:
                user_input = int(user_input)-1
                if user_input <= len(_option_list)-1 and user_input >= 0:
                    valid = True
                    return user_input
                else:
                    raise TypeError
            except:
                valid = False
                print('Invalid selection, please try again.')

def number_input(_type:type = int, _input_text:str = "Number: ", _lower_bound: int|float|type = None, _upper_bound: int|float|type = None) -> float|int:
    while True:
        user_input = input(_input_text)
        try:
            if _type == int:
                user_input = int(user_input)
            elif _type == float:
                user_input = float(user_input)
            else:
                raise
            potentially_valid = False
            if _lower_bound != None:
                if user_input >= _lower_bound:
                    potentially_valid = True
            else:
                potentially_valid = True
            if _upper_bound != None and potentially_valid:
                if user_input <= _upper_bound:
                    return user_input
        except:
            if _type == int:
                print(user_input + " is not a valid integer")
            elif _type == float:
                print(user_input + " is not a valid float")
            else:
                print('Invalid attempted type forcing')


def print_table(_table:list, left_buffer:int = 1, right_buffer:int = 0, has_labels:bool = False) -> None:
    for i in range(0,len(_table[0])):
        locals()[i] = 0
    for row in _table:
        item_num = 0
        for item in row:
            if locals()[item_num] < len(str(item)):
                locals()[item_num] = len(str(item))
            item_num += 1
    header_string = ' '
    for i in range(0,len(_table[0])):
        header_string = header_string + '_' * (locals()[i]+left_buffer+right_buffer+1)
    header_string = header_string[:-1]
    print(header_string)
    label_string = '|'
    for colum_num in range(0, len(_table[0])):
            label_string = label_string + '‾' * (locals()[colum_num]+left_buffer+right_buffer) + '|'
    first_row = True
    for row in _table:
        row_string = '|' + ' ' *left_buffer
        item_num = 0
        for item in row:
            row_string = row_string + str(item) + ' ' * (locals()[item_num]-len(str(item))) + ' ' * right_buffer + '|'  + ' ' * left_buffer
            item_num += 1
        print(row_string)
        if has_labels and first_row:
            print(label_string)
        first_row = False
    footer_string = header_string.replace('_', '‾')
    print(footer_string)
        