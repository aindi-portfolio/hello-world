#Scenario 1

# Linear Search
def linear_search_unsorted(lst:list, target:int):
    iterations = 0
    for index, value in enumerate(lst):
        iterations += 1
        if value == target:
            return index, iterations
    return None, iterations  # Target not found    


# Binary Search
def binary_search_unsorted(lst:list, target:int):
    lst = sorted(lst)  # Ensure the list is sorted for binary search
    start = 0
    end = len(lst) - 1
    iterations = 0
    while start <= end:
        iterations += 1
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid, iterations
        elif lst[mid] < target:
            start = mid + 1
        elif lst[mid] > target:
            end = mid - 1
    return None, iterations



# Scenario 1 Test
# unsorted_list = [42, 15, 7, 30, 22, 10, 18]
# target_1 = 23
# result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
# result_binary_search_1 = binary_search_unsorted(unsorted_list, target_1)
# print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
# print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")


# Scenario 2

# Linear Search
def linear_search_sorted_words(word_list, target_word):
    iterations = 0
    for index, word in enumerate(word_list):
        iterations += 1
        if word == target_word:
            return index, iterations
    return None, iterations

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    left = 0
    right = len(word_list) - 1
    iterations = 0
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if word_list[mid] == target_word:
            return mid, iterations
        elif word_list.index(target_word) < mid:
            right = mid - 1
        elif word_list.index(target_word) > mid:
            left = mid + 1
    return None, iterations

# Scenario 2 Test
# sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
# target_2 = 'orange'
# result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
# result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
# print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
# print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")


# Secnario 3

# Linear Search
def linear_search_last_occurrence(arr, target):
    # iterations = 0
    # num_holder = None
    # for index, value in enumerate(arr):
    #     iterations += 1
    #     if index == len(arr) - 1 and index:

    #     if value == target:
    #         print(index, iterations)
    #         if num_holder == None:
    #             num_holder = arr.index(value)
    #         else:
    #             if num_holder

    # return None, iterations
    pass

# Binary Search
def binary_search_last_occurrence(arr, target):
    arr = sorted(arr)


    pass

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
# print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
# print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")