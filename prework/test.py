good_numbers = [1,2,3,4,5,6,7,8,9]
opposite_numbers = [9,8,7,6,5,4,3,2,1]
random_numbers = [42,1,89,5]
more_numbers = [10,11,12,13,14,15]

def is_consecutive(a_list):
    """Checks to see if numbers are consecutive"""
    list_copy = a_list[:]
    for copy in list_copy:
        consecutive = copy + 1
        break
    for number in a_list:
        if number + 1 == consecutive:
            number += 1
            consecutive += 1
        else:
            return False
    return True

print(is_consecutive(good_numbers))
print(is_consecutive(opposite_numbers))
print(is_consecutive(random_numbers))
print(is_consecutive(more_numbers))