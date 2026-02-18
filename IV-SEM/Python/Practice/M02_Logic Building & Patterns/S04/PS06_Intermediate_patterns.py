'''
#1.traditinal method for doubling the numbers
li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i*2)
print(res)
# list comprehension method
print([i*2 for i in li])

#2.inding even numbers in a list
li = [1,2,3,4,5]
res = []
for i in li:
    if i%2==0:
        res.append(i)
print(res)
 
#with list comprehension 
print([i for i in li if i%2==0])

#3.traditional metod of joining 
li = ['a','b','c']
str = ""
for i in li:
    str+=i 
print(str)
#using join method
print("".join(li))
'''
'''Intermediate patterns
1. Pyramid
n = 4
output:
    *
   * *
  * * *
 * * * *

n = int(input())
for i in range(1,n+1):
    print((n-i)*" "+i*"* ")
'''
'''
inverted pyramid
#n = 4
#output:

* * * * 
 * * * 
  * * 
   * 
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(i-1)+"* "*(n-i+1))



