#Author - MIKAIL RAJA
#Data of Compilation - 21/01/2022
#Title - Given a number, find the sum of all even and odd digits present in the number

n = input().strip()
even_sum = 0
odd_sum = 0
for i in n:
    if int(i) % 2 == 0:
        even_sum += int(i)
    else:
        odd_sum += int(i)

print(even_sum, odd_sum)