# 1. Count Occurrences
def count_occurrences(lst, element):
    return lst.count(element)

# 2. Sum of Elements
def sum_of_elements(lst):
    return sum(lst)

# 3. Max Element
def max_element(lst):
    return max(lst) if lst else None

# 4. Min Element
def min_element(lst):
    return min(lst) if lst else None

# 5. Check Element
def check_element(lst, element):
    return element in lst

# 6. First Element
def first_element(lst):
    return lst[0] if lst else None

# 7. Last Element
def last_element(lst):
    return lst[-1] if lst else None

# 8. Slice List
def slice_list(lst):
    return lst[:3]

# 9. Reverse List
def reverse_list(lst):
    return lst[::-1]

# 10. Sort List
def sort_list(lst):
    return sorted(lst)

# 11. Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))

# 12. Insert Element
def insert_element(lst, index, element):
    lst.insert(index, element)

# 13. Index of Element
def index_of_element(lst, element):
    return lst.index(element) if element in lst else -1

# 14. Check for Empty List
def is_empty(lst):
    return len(lst) == 0

# 15. Count Even Numbers
def count_even_numbers(lst):
    return len([x for x in lst if x % 2 == 0])

# 16. Count Odd Numbers
def count_odd_numbers(lst):
    return len([x for x in lst if x % 2 != 0])

# 17. Concatenate Lists
def concatenate_lists(lst1, lst2):
    return lst1 + lst2

# 18. Find Sublist
def find_sublist(lst, sublist):
    return str(sublist) in str(lst)

# 19. Replace Element
def replace_element(lst, old_element, new_element):
    if old_element in lst:
        index = lst.index(old_element)
        lst[index] = new_element

# 20. Find Second Largest
def find_second_largest(lst):
    return sorted(set(lst))[-2] if len(set(lst)) > 1 else None

# 21. Find Second Smallest
def find_second_smallest(lst):
    return sorted(set(lst))[1] if len(set(lst)) > 1 else None

# 22. Filter Even Numbers
def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# 23. Filter Odd Numbers
def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

# 24. List Length
def list_length(lst):
    return len(lst)

# 25. Create a Copy
def create_copy(lst):
    return lst.copy()

# 26. Get Middle Element
def get_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    return lst[n//2] if n % 2 != 0 else lst[n//2-1:n//2+1]

# 27. Find Maximum of Sublist
def max_of_sublist(lst, start, end):
    return max(lst[start:end+1]) if start < len(lst) and end < len(lst) else None

# 28. Find Minimum of Sublist
def min_of_sublist(lst, start, end):
    return min(lst[start:end+1]) if start < len(lst) and end < len(lst) else None

# 29. Remove Element by Index
def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]

# 30. Check if List is Sorted
def is_sorted(lst):
    return lst == sorted(lst)

# 31. Repeat Elements
def repeat_elements(lst, times):
    return [x for x in lst for _ in range(times)]

# 32. Merge and Sort
def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

# 33. Find All Indices
def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

# 34. Rotate List
def rotate_list(lst, k):
    return lst[-k:] + lst[:-k] if lst else []

# 35. Create Range List
def create_range_list(start, end):
    return list(range(start, end+1))

# 36. Sum of Positive Numbers
def sum_positive_numbers(lst):
    return sum(x for x in lst if x > 0)

# 37. Sum of Negative Numbers
def sum_negative_numbers(lst):
    return sum(x for x in lst if x < 0)

# 38. Check Palindrome
def is_palindrome(lst):
    return lst == lst[::-1]

# 39. Create Nested List
def create_nested_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

# 40. Get Unique Elements in Order
def get_unique_elements(lst):
    seen = set()
    return [x for x in lst if x not in seen and not seen.add(x)]
