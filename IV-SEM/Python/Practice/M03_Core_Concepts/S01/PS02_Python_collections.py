'''#running sum
nums = list(map(int,input().split()))
sum1 = 0
res = []
for i in range(len(nums)):
    sum1 +=nums[i]
    res.append(sum1)
print(res)
# input:1 2 3 4 5
# output:[1, 3, 6, 10, 15]
#duplicates
arr = list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]!=arr[i+1]:
        print("false")
    else:
        print("true")
Sets:
1) Definition: A set is an unordered collection of unique elements. It is defined using curly braces {} or the built-in set() function.
2) Creation : set()
3)Adding: add() method is used to add an element to a set. If the element already exists, it will not be added again, as sets do not allow duplicates.
4) Removing: remove() method is used to remove an element from a set. If the element does not exist, it raises a KeyError. The discard() method can also be used to remove an element, but it does not raise an error if the element is not found.
5) Set Operations: union,intersection,difference,symmetric_difference

a = set([1, 2, 3, 4, 5])
print(a)
a.add(6)
a.add(5)
a.remove(3)
print(a)
b = set([4, 5, 6, 7, 8])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))'''
'''
#TUPLES:
1) Definition: A tuple is an ordered collection of elements that is immutable, meaning its
2) Immutable: Once a tuple is created, its elements cannot be modified. This immutability allows tuples to be used as keys in dictionaries and elements of sets.
3)Accessing Elements: Tuples support indexing and slicing to access individual elements or subsequences of elements.
4) Concatenation of tuples:
5)Repetition of tuples
6)Nesting of tuples:
7) Slicing of tuples:
8) Deleting a tuple:

t = (1, 2, 3, 4, 5)
print(t)
#2) Immutable
t = (1,2,3,4,5)
t[0] = 10 # This will raise a TypeError because tuples are immutable
print(t)
#4) Concatenation of tuples:
t = (1, 2, 3, 4, 5)
t2 = (6, 7,3, 8, 9, 10)
print(t + t2)

#5) Repetition of tuples
t = (1,2,3,4,5,6,)
print(t*2) 
#6)Nesting of tuples:
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print((t1, t2))
#7) Slicing of tuples:
t = (1, 2, 3, 4, 5)
print(t[1:])
print(t[0:4])
#8) Deleting a tuple:
t = (1, 2, 3, 4, 5)
del t
 # This will create a new tuple that contains the elements from

#DICTIONARIES:
1) Definition: A dictionary is an unordered collection of key-value pairs. It is defined using curly braces {} and consists of keys and their corresponding values.
2) Creation: A dictionary can be created using curly braces {} with key-value pairs separated by colons, or by using the built-in dict() function.
3)Accessing dict items:
4) Adding and updating items:
5)Removing items
6)

#2) Creation:({},dict())
d = {"name": "Alice", "age": 30, "city": "New York"}
print(d)
d1 = dict(name="Alice", age=30, city="New York")
print(d1)

#3)Accessing dict items:
d = {"name": "Alice", "age": 30, "city": "New York"}
print(d.get('name'))
print(d.keys())
print(d.values())

#4) Adding and updating items:
d = {"name": "Alice", "age": 30, "city": "New York"}
d['phn']= 12345
print(d)
d['age'] = 31
print(d)
'''
#5)Removing items(del,pop(),popitem(),clear())
d = {"name": "Alice", "age": 30, "city": "New York"}
del d['age']
print(d)
print(d.pop('city'))
print(d.popitem())
d.clear()
print(d)