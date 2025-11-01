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
