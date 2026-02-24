number_of_elements = input("Enter the number of elements in the list: ")
inputs = list(map(int, input("Enter the elements separated by space: ").split()))

def analyze_numbers(numbers):
    unique_numbers = set(numbers)
    duplicate_numbers = set(x for x in numbers if numbers.count(x) > 1)
    frequency_dictionary = {num: numbers.count(num) for num in unique_numbers} 
    most_frequent_number = max(frequency_dictionary, key=frequency_dictionary.get)
    least_frequent_number = min(frequency_dictionary, key=frequency_dictionary.get)    
    return unique_numbers, duplicate_numbers, frequency_dictionary, most_frequent_number, least_frequent_number

unique_numbers, duplicate_numbers, frequency_dictionary, most_frequent_number, least_frequent_number = analyze_numbers(inputs)
print(f"Unique numbers: {unique_numbers}")
print(f"Count of unique numbers: {len(unique_numbers)}")
print(f"Duplicate numbers: {duplicate_numbers}")
print(f"Frequency dictionary: {frequency_dictionary}")
print(f"Most frequent number: {most_frequent_number}")
print(f"Least frequent number: {least_frequent_number}")    