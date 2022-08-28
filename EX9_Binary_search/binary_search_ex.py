# numbers = [1,4,6,9,10,5,7]

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def find_ocrns(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    index_list = []
    pre_index = index - 1
    post_index = index + 1    
    while numbers[pre_index] == number_to_find:
        index_list.append(pre_index)
        pre_index-=1    
    while numbers[post_index] == number_to_find:
        index_list.append(post_index)
        pre_index+=1
    print(index_list)    

if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  

# x = binary_search(numbers, number_to_find)    
# print(x)

    y = find_ocrns(numbers, number_to_find)
    print(y)

print(10)    