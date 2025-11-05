               # List in Python 
---
Q. **Program to create and display a list**

```python
# Creating the list "thislist"  
thislist = ["apple" , "banana" , "Cherry"]  
  
# Printing the list 
print(thislist)
```

**Example 2:**
```python
# Creating the list "thislist"  
my_list = [10, 20, 30, 40, 50]  
  
# Printing the list 
print("the created list is: ", my_list)

```

**List (imp points)**
Perfect summary 👍

Let’s put all that information into a **clear explanation format** (useful for notes or BCA practical theory):

---

### **Definition**

A **list** in Python is a collection used to store multiple items in a single variable.  
Lists are written using **square brackets [ ]** and can hold items of **different data types**.

Example:

```python
fruits = ["apple", "banana", "cherry"]
```

---

### **Properties of Lists**

#### 1. **Ordered**

- The items in a list have a defined **order**.
- Each item’s position (index) will **not change** unless you modify the list.
- The first item has index **0**, the second **1**, and so on.

Example:

```python
numbers = [10, 20, 30]
print(numbers[0])  # Output: 10
```

---

#### 2. **Changeable (Mutable)**

- You can **add**, **remove**, or **change** items after the list is created.

Example:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"     # Change item
fruits.append("orange") # Add new item
print(fruits)
# Output: ['apple', 'mango', 'cherry', 'orange']
```

---

#### 3. **Allow Duplicates**

- Lists can contain **duplicate values** since each item has its own index.

Example:

```python
names = ["Kavya", "Kavya", "Jain"]
print(names)
# Output: ['Kavya', 'Kavya', 'Jain']
```

---

Q. **Program to find sum and average of list elements**

```python
# Program to find sum and average of list elements

# Create the list 
numbers = [10,20,30,40,50]

# Calculate the sum 
total = sum(numbers)

# Calculate the avg 
average = total/len(numbers)

#Print the values
print("List: " , numbers)
print("Sum of list: ", total)
print("avg of list: ", average)

```

### **Algorithm:**
1. Start the program.
2. Create a list of numbers.
3. Use the built-in `sum()` function to find the total of list elements.
4. Use `len()` to find the number of elements in the list.
5. Calculate average = sum / number of elements.
6. Display the sum and average.
7. Stop the program.

---
Q. **1. Program to find largest and smallest element in a list**

```python
# Program to find largest and smallest element in a list  
  
# Create the list  
numbers = [10,23,45,67,43,53,35,6,64]  
  
# find smallest and largest item  
largest = max(numbers)  
smallest = min(numbers)  
  
#print the smallest and largest  
print("The smallest item in list is: " , smallest)  
print("The largest item in list is: " , largest)
```

### **Algorithm:**

1. Start the program.
2. Create a list containing numerical elements.
3. Use the built-in `max()` function to find the largest element.
4. Use the built-in `min()` function to find the smallest element.
5. Display the largest and smallest elements.
6. Stop the program

---
Q. **Program to count even and odd numbers in a list**

```python
# Program to count even and odd numbers in a list  
  
# Create the list  
numbers = [10, 23,4,5,24,53,43,2,5,43,56,78]  
  
# Intialize counters  
even_count = 0  
odd_count = 0  
  
# Traverse the list  
for num in numbers :  
    if num % 2 == 0 :  
        even_count += 1  
    else :  
        odd_count += 1  
  
# Display even odd count  
print ("list: " , numbers)  
print("Even count: ", even_count)  
print("Odd count: " , odd_count)
```

### **Algorithm:**

1. Start the program.
2. Create a list containing numerical elements.
3. Initialize two counters: `even_count` and `odd_count` to zero.
4. Use a loop to traverse each element in the list.
5. For each element:
    - If the number is divisible by 2, increment `even_count`.
    - Else, increment `odd_count`.
6. Display the total count of even and odd numbers.
7. Stop the program.

---
Q.  **Program to remove duplicates from a list**

```python
# Program to remove duplicates from a list  
  
# Create list  
numbers = [10,10,20,30,30,20,30,40,50,60,60]  
  
# Remove duplicates  
unique_numbers = list(set(numbers))  
  
# Display  
print("Original list: " , numbers)  
print("Removed duplicates list: ", unique_numbers)
```

### **Algorithm:**

1. Start the program.
2. Create a list that contains duplicate elements.
3. Convert the list into a **set** to automatically remove duplicates (since sets do not allow duplicate values).
4. Convert the set back into a **list**.
5. Display the new list without duplicates.
6. Stop the program.

---
Q. **Program to sort and reverse a list**

```python
# Sort & reverse a list  
  
# Create a list  
numbers = [25, 10, 45, 30, 5, 60]  
  
# Sort list in ascending order  
numbers.sort()  
print("list after sorting: ", numbers)  
  
# Reverse the list  
numbers.reverse()  
print("list after reversing: ", numbers)
```

### **Algorithm:**

1. Start the program.
2. Create a list with numerical elements.
3. Use the `sort()` function to arrange the list elements in **ascending order**.
4. Use the `reverse()` function to reverse the order of elements.
5. Display the sorted and reversed lists.
6. Stop the program.

---
# Tuples & Set 
---
## 🧾 **Tuple in Python**

### **Definition:**

A **tuple** in Python is a collection used to store multiple items in a single variable.  
Tuples are written using **round brackets ( )**, for example:

```python
fruits = ("apple", "banana", "cherry")
```

---

### **Properties of Tuples**

#### 🟠 1. **Ordered**

- The items in a tuple have a **defined order**, which means their position is fixed.
- Indexing starts from **0** — the first item has index `0`, the second `1`, and so on.
- The order **will not change** unless a new tuple is created.
**Example:**

```python
numbers = (10, 20, 30)
print(numbers[0])  # Output: 10
```

---

#### 🟣 2. **Unchangeable (Immutable)**

- Once a tuple is created, its elements **cannot be changed, added, or removed**.
- This immutability makes tuples faster and safer than lists when you want data to remain constant.

**Example:**

```python
fruits = ("apple", "banana", "cherry")
# fruits[1] = "mango"  ❌  This will cause an error
```

---

#### 🔵 3. **Allow Duplicates**

- Tuples can contain **duplicate values** because each item is stored at a specific index.

**Example:**

```python
colors = ("red", "blue", "red", "green")
print(colors)
# Output: ('red', 'blue', 'red', 'green')
```

---
Q. **Program to create and access tuple elements**

```python
# Program to create and access tuple elements  
  
# Create the list  
fruits = ("apple", "banana", "cherry", "mango", "orange")   # Curly braces for tuple  
  
# Display the tuple  
print("Tuple Elements: ", fruits)  
  
# Access elements using indexing  
print("First element: ", fruits[0])  
print("third element: ", fruits[2])  
print("last element: ", fruits[-1])  
  
# Access elements using slicing  
print("Elements from index 1 to 3:", fruits[1:4])
```

### **Algorithm:**

1. Start the program.
2. Create a tuple containing some elements (numbers, strings, etc.).
3. Access elements using **indexing** (e.g., `tuple_name[index]`).
4. Access multiple elements using **slicing** (e.g., `tuple_name[start:end]`).
5. Display the results.
6. Stop the program.

---
Q. Program to find the length of a tuple

```python
# Program to find the length of a tuple  
  
# Create the list  
fruits = ("apple", "banana", "cherry", "mango", "orange")  
  
# Find length of tuple  
length = len(fruits)  
  
# Display  
print("Tuple elements: " , fruits)  
print("length of tuple: ", length)
```

### **Algorithm:**

1. Start the program.
2. Create a tuple with some elements.
3. Use the built-in function `len()` to find the number of elements in the tuple.
4. Display the length of the tuple.
5. Stop the program.

---
# Sets
---
Excellent summary 👏  
Here’s how you can write it neatly in **BCA theory or practical file format** — with clear explanations and examples 👇

---

## 🧾 **Set in Python**

### **Definition:**

A **set** in Python is a collection used to store **multiple items** in a single variable.  
Sets are written using **curly brackets `{ }`**.  
Example:

```python
fruits = {"apple", "banana", "cherry"}
```

---

### **Properties of Sets**

#### 🔸 1. **Unordered**

- The elements in a set **do not have a fixed order**.
- Each time you print or access a set, the items may appear in a **different order**.
- Since sets are unordered, **they cannot be accessed using indexes**.

**Example:**

```python
numbers = {10, 20, 30, 40}
print(numbers)
# Output may appear as {40, 10, 20, 30}
```

---

#### 🔸 2. **Unchangeable**

- Once a set is created, its **items cannot be changed**.
- However, you can **add or remove** items (you just can’t modify an existing one).

**Example:**

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("mango")   # Add new item
fruits.remove("banana")  # Remove an item
print(fruits)
```

---

#### 🔸 3. **Duplicates Not Allowed**

- Sets **do not allow duplicate values**.
- If duplicate items are included, Python automatically removes the duplicates.

**Example:**

```python
colors = {"red", "blue", "red", "green"}
print(colors)
# Output: {'red', 'green', 'blue'}
```

---

Q. **Program to demonstrate union, intersection, and difference of sets**

```python
# Program to demonstrate union, intersection, and difference of sets  
  
# Create set  
set1 = {1, 2, 3, 4, 5}  
set2 = {4, 5, 6, 7, 8}  
  
# Perform set operations  
union_set = set1.union(set2)  
intersection_set = set1.intersection(set2)  
difference_set = set1.difference(set2)  
  
# Display  
print("Set 1:", set1)  
print("Set 2:", set2)  
print("Union of sets:", union_set)  
print("Intersection of sets:", intersection_set)  
print("Difference of sets (Set1 - Set2):", difference_set)
```

### **Algorithm:**

1. Start the program.
2. Create two sets with some common and unique elements.
3. Perform:
    - **Union:** Combine all elements from both sets (no duplicates).
    - **Intersection:** Display only common elements between sets.
    - **Difference:** Display elements present in one set but not in the other.
4. Display the results of all three operations.
5. Stop the program.

---
# Dictionaries
---
### 🧠 **Python Dictionary **

**1. Definition:**  
A **dictionary** stores data in **key: value pairs**.  
It’s like a real dictionary where you look up a word (key) to find its meaning (value).

Example:

```python
student = {
  "name": "Kavya",
  "age": 20,
  "course": "BCA"
}
print(student)
```

---

**2. Ordered (from Python 3.7+):**  
Dictionaries remember the order you add items in.  
That means items will stay in the same sequence.

---

**3. Changeable:**  
You can **add**, **update**, or **remove** key-value pairs after creation.

Example:

```python
student["age"] = 21     # Update value
student["grade"] = "A"  # Add new key-value pair
del student["course"]   # Remove a key-value pair
print(student)
```

---

**4. No Duplicates:**  
Each **key** must be unique.  
If you use the same key twice, the last value will replace the previous one.

Example:

```python
student = {
  "name": "Kavya",
  "name": "Aarav"
}
print(student)   # Output: {'name': 'Aarav'}
```

---

**5. Accessing Elements:**  
Use the key name inside square brackets or the `.get()` method.

Example:

```python
print(student["name"])      # Direct access
print(student.get("grade")) # Safe access
```

---
 Q. **Program to create a dictionary and access elements**
```python
# Program to create a dictionary and access elements  
  
# Create a dict  
student = {  
    "name": "Kavya",  
    "age": 20,  
    "course": "BCA",  
    "year": 2025  
}  
  
# Display the entire dictionary  
print("Student dictionary: ", student)  
  
# Accessing the elements  
print("Name:", student["name"])  
print("Age:", student["age"])  
print("Course:", student["course"])  
print("Year:", student["year"])  
  
# Accessing using get() method  
print("Access using get():", student.get("course"))
```

### 🧠 **Algorithm: Create and Access Dictionary Elements**

1. **Start**
2. **Create** an empty or predefined dictionary using curly braces `{}`.  
    Example:  
    `student = {"name": "Kavya", "age": 20, "course": "BCA", "year": 2025}`
3. **Display** the entire dictionary using the `print()` function.
4. **Access** individual elements using their **keys**, e.g. `student["name"]`.
5. **Optionally**, access elements using the `get()` method, e.g. `student.get("course")`.
6. **Display** the accessed values on the screen.
7. **Stop**

---
Q. **Program to add and remove elements from a dictionary**

```python
# Program to add and remove elements from a dictionary  
  
# Creating a dictionary  
student = {  
    "name": "Kavya",  
    "age": 20,  
    "course": "BCA"  
}  
  
print("Original Dictionary:", student)  
  
# Adding elements  
student["year"] = 2025  
student["grade"] = "A"  
print("After Adding Elements:", student)  
  
# Removing an element using pop()  
student.pop("age")  
print("After Removing 'age':", student)  
  
# Removing last inserted item using popitem()  
student.popitem()  
print("After Removing Last Item:", student)  
  
# Removing an element using del  
del student["course"]  
print("After Deleting 'course':", student)
```

### 🧠 **Algorithm: Add and Remove Elements from a Dictionary**

1. **Start**
2. **Create** a dictionary with some initial key-value pairs.
3. **Display** the original dictionary.
4. **Add** new key-value pairs using assignment (`dict[key] = value`).
5. **Remove** an element using the `pop()` method (removes by key).
6. **Remove** the last inserted item using `popitem()`.
7. **Remove** an element using the `del` statement.
8. **Display** the dictionary after each operation.
9. **Stop**

---
Q. **Program to count frequency of elements using dictionary**

```python 
# Program to count frequency of elements using dictionary  
  
# Creating a list  
numbers = [2, 4, 2, 8, 4, 4, 6, 2, 8]  
  
# Creating an empty dictionary  
frequency = {}  
  
# Counting frequency of each element  
for item in numbers:  
    if item in frequency:  
        frequency[item] += 1  
    else:  
        frequency[item] = 1  
  
# Displaying the frequency of elements  
print("List:", numbers)  
print("Frequency of elements:", frequency)
```

### 🧠 **Algorithm: Count Frequency of Elements Using Dictionary**

1. **Start**
2. **Initialize** a list with some elements.
3. **Create** an empty dictionary to store the frequency count.
4. **Repeat** for each element in the list:
    - If the element is already a key in the dictionary, **increment** its value by 1.
    - Else, **add** the element to the dictionary with value 1.
5. **Display** the dictionary showing element-frequency pairs.
6. **Stop**

----
Q. **Program to find student’s highest and lowest marks using dictionary**

```python
# Program to find student's highest and lowest marks using dictionary

# Creating a dictionary of subjects and marks
marks = {
    "Math": 88,
    "Science": 92,
    "English": 79,
    "Computer": 95,
    "History": 85
}

# Display the dictionary
print("Student Marks:", marks)

# Finding the subject with highest and lowest marks
highest_subject = max(marks, key=marks.get)
lowest_subject = min(marks, key=marks.get)

print("Highest Marks:", highest_subject, "=", marks[highest_subject])
print("Lowest Marks:", lowest_subject, "=", marks[lowest_subject])

```

### 🧠 **Algorithm: Find Student’s Highest and Lowest Marks Using Dictionary**

1. **Start**
2. **Create** a dictionary with subject names as keys and marks as values.
3. **Display** the dictionary.
4. **Find the key** (subject) having the highest marks using `max(dictionary, key=dictionary.get)`.
5. **Find the key** having the lowest marks using `min(dictionary, key=dictionary.get)`.
6. **Display** the subject and marks for both highest and lowest values.
7. **Stop**



