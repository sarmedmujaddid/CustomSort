import re
def custom_sort(string):
    numbers = re.findall(r'\d+', string)
    numbers = sorted(numbers, key=int)
   
    lowercase = sorted([ch for ch in string if ch.islower()])
    uppercase = sorted([ch for ch in string if ch.isupper()])
    others = sorted([ch for ch in string if not ch.isalnum()])
    return "".join(numbers + lowercase + uppercase + others)

# Example usage
#input_str = "08s31a*&bDfK41BAl1"
#input_str = "A11a4"
input_str = input("Enter input: ")
output_str = custom_sort(input_str)
print(output_str)
