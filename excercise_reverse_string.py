
def reverse_string(string_to_reverse):
    string_reversed = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_reversed

# def biggest_number_of_three(first, second, third):


print(reverse_string("Hola"))
print(reverse_string("Cocacola"))
print(reverse_string("Games"))
print(reverse_string("Food"))
print(reverse_string("Chicken"))