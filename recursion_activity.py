Hands-On Activity: Recursive Array Toolkit

def sum_array(numbers):

    
    if len(numbers) == 0:
        return 0

    
    return numbers[0] + sum_array(numbers[1:])




def find_largest(numbers):

    if len(numbers) == 0:
        raise ValueError("The array must not be empty.")

    if len(numbers) == 1:
        return numbers[0]

    largest_of_rest = find_largest(numbers[1:])

    if numbers[0] > largest_of_rest:
        return numbers[0]

    return largest_of_rest



def count_number(numbers, target):

    
    if len(numbers) == 0:
        return 0

    
    current_count = 1 if numbers[0] == target else 0

    return current_count + count_number(numbers[1:], target)




print("1. SUM THE ARRAY")
print("Empty array:", sum_array([]))
print("One number:", sum_array([7]))
print("Several numbers:", sum_array([4, -2, 8, -5]))

print("\n2. FIND THE LARGEST NUMBER")
print("One number:", find_largest([9]))
print("Largest at beginning:", find_largest([15, 3, 8, 2]))
print("Largest at end:", find_largest([-8, -3, -10, -1]))
print("Negative numbers:", find_largest([-9, -4, -12]))

print("\n3. COUNT A CHOSEN NUMBER")
print("Empty array:", count_number([], 5))
print("Target appears several times:",
      count_number([2, 5, 2, 7, 2, 9], 2))
print("Target does not appear:",
      count_number([1, 3, 4, 6], 8))
