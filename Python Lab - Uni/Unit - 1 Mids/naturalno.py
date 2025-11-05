# Sum of first N Natural numbers
N = int(input("Enter a number: "))

sum = 0

for i in range (1, N+1):
    sum = sum + i

print(sum)