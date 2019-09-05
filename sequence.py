n = int(input("Enter the length of the sequence:  "))

count_number = 3
num1 = 1
num2 = 2
num3 = 3

while count_number <= n:
    sum = num1 + num2 + num3
    print(sum)
    count_number += 1

    num1 = num2
    num2 = num3
    num3 = sum  