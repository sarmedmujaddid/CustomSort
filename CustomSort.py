import re #importing regular expression module
def custom_sort(string):

    # Extract numbers as whole values and sort them
    numbers = re.findall(r'\d+', string)
    numbers = sorted(numbers, key=int)
   
    # Extract and sort lowercase, uppercase, and other special characters separately 
    lowercase = sorted([ch for ch in string if ch.islower()])
    uppercase = sorted([ch for ch in string if ch.isupper()])
    others = sorted([ch for ch in string if not ch.isalnum()])

    # Combine sorted groups into the final string
    return "".join(numbers + lowercase + uppercase + others)

#input_str = "A11a4"
input_str = input("Enter Input: ")
output_str = custom_sort(input_str)
print(f"Output: {output_str}")
