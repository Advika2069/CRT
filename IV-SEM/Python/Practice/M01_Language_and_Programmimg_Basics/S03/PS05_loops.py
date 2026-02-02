# Accept a number(n) from the user and display 1-n natural numbers in the same line
n = int(input())
i = 1
while i <= n:
    print(i,end=" ")
    i += 1
print()
j = n
while j >= 1:
    print(j,end=" ")
    j -= 1