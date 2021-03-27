def binary_search(num_list, search_value):

    lower_bound = num_list[0]
    upper_bound = num_list[len(num_list) - 1]

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) / 2
        value_at_midpoint = num_list[midpoint]

        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1

        return None


print(binary_search([1, 2, 3, 4, 5], 2))
