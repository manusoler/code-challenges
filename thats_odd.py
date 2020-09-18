# Find the sum of all even integers in a list of numbers
size = int(input())
sum = 0
for i in range(size):
    num = int(input())
    sum += num if num % 2 == 0 else 0
print(sum)