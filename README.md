# 🔠 Alphanumeric Sort Algorithm
This project implements an Alphanumeric Sorting Algorithm in Python. The sorting logic follows these rules:

1. Numbers come first (consecutive digits are treated as a single number).
2. Followed by lowercase letters (a-z).
3. Then uppercase letters (A-Z).
4. Finally, special characters (non-alphanumeric characters like @, #, *, etc.).


### 📥 Example Input & Output:
``` bash

Input:  A11a4  
Output: 411aA

```

### 🚀 Features
✅ Handles multi-digit numbers as single entities.

✅ Maintains sorting order for different character groups.

✅ Accepts dynamic user input via the terminal.

✅ Clean, readable code with regular expressions for efficient parsing.


### 📦 Project Structure

```plaintext

alphanumeric-sort/
├── custom_sort.py     # Main Python script for sorting
├── README.md          # Documentation
└── .gitignore         # Git ignored files (optional)

```

### ⚙️ How to Run the Project

#### 1️⃣ Prerequisite
- Python 3.x (Download from https://www.python.org/downloads/)
- VS Code or any Python IDE
  
#### 2️⃣ Clone the Repository

```bash

git clone https://github.com/sarmedmujaddid/CustomSort.git
cd CustomSort
```

#### 3️⃣ Run the Script

```bash
python CustomSort.py
```


#### 4️⃣ Example Run

```bash

Enter input: A11a4
Output: 411aA
```

#### 📝 Code Explanation (custom_sort.py)

```python

import re

def custom_sort(string):
    # Extract numbers as whole values and sort them
    numbers = re.findall(r'\d+', string)
    numbers = sorted(numbers, key=int)

    #Extract and sort lowercase, uppercase, and other special characters separately

    lowercase = sorted([ch for ch in string if ch.islower()])
    uppercase = sorted([ch for ch in string if ch.isupper()])
    others = sorted([ch for ch in string if not ch.isalnum()])

    # Combine sorted groups into the final string
    return "".join(numbers + lowercase + uppercase + others)


# User input from terminal
#input_str = "A11a4"
input_str = input("Enter Input: ")
output_str = custom_sort(input_str)
print(f"Output: {output_str}")

```

#### 📊 Sample Test Cases

| Input	|                    Expected Output |
| -------------              | ------------- |
| A11a4 |                              411aA |
| 08s311a*&bDfK41BAl19 | 081941311abflsABDK&* |
| zZyYxX1@!2#3$	| 123xyzXYZ!#$@ |
| B2aA4dD!@1cC3 |	1234acdABCD!@ |


#### 🔐 Best Practices & Design Decisions
- Regular Expressions (re.findall) are used for efficient numeric extraction.
- List Comprehension for clean, readable code.
- Maintains modularity for easy updates or feature additions.

