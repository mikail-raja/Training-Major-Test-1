#Author - MIKAIL RAJA
#Data of Compilation - 21/01/2022
#Title - Find the minimum natural number not present in given list

n = int(input())
li = list(map(int,input().split()))
nat = int(-1)
for i in range(1,max(li)):
    if i not in li:
        nat = i
        break

if(nat == -1):
    print(max(li)+1)
else:
    print(nat)