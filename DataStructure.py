#LISTS: Ordered, changeable, and allow duplicate values.
"""
list1 = [1, 3, 34, 7, 8, 298, 9]   

#l = list1.sort(reverse=True)
#print(l)
list1.append(4)
print(list1)
print(type(list1))
print(list1[-1])
print(len(list1))  #length
print(list1[3:-1]) #Slicing
print(list1[1:5:2]) #Jump
lc = [i for i in range(5)]  #List Comprehension
print(lc)

"""
"""
#Exercise1 - Lists: KBC
print("Your Question for $10,000 is on the screen:\n")

Questions = print("Q1] What is captial of India?")
print("Your Options are as follows:")
Options = print("A) Delhi"," B) Mumbai", "C) Kolkata", "D) Chennai\n")

Answers = ["Delhi","Mumbai","Kolkata","Chennai"]
x = input("Enter your Answer: ")
if x == Answers[0]:
    print("CONGRATULATIONS, You have won $10,000!!!!")
else:
    print("Unfortunately, you have lost this round.")

"""

#TUPLE: Ordered, unchangeable, and allow duplicate values.
"""
tuple1 = (1, 548, 8, 9, 53, 7, 10)  
print(tuple1)
mylist = list(tuple1)
mylist.pop(2) 
tuple1 = tuple(mylist)  
print(tuple1)
print(tuple1[-3:-1])
if 548 in tuple1:
    print("The num 548 present.")

"""
#Exercise: Tuple
"""dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
print(dji1 + dji2)"""

#SETS: Unordered, unchangeable, and do not allow duplicate values.
"""
set1 = {'orange', 'apple','banana', 'fig', 'kiwi'}   
set2 = {'may', 'june', 'july', 'fig'}
set1.add('pineapple')
# set1.update(set2)
print(set1.union(set2))
print(set1.symmetric_difference(set2))
print(set1.intersection(set2))
print(set1.isdisjoint(set2))
"""
#Exercise: Sets

"""text = 'Programming in python.'
text = text.lower()
text = text.replace(" ","") 
text = text.replace(".","") 
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = set(text)
const = letters.difference(vowels)
print(f"Number of items: {len(const)}")
"""

# DICTIONARY: Ordered, changeable, and does not allow duplicates.
"""
dict1 = {2:'Merin', 33:'Neymar', 28:'OurCHild'} 
dict2 ={4:'Mon', 3:'Tue', 19:'Wed'}
dict1[28]='Football'
dict1[21]='ronaldo'
print(dict1)
print(dict1.get(33))
print(dict1.keys())
print(dict1.items())

for x in dict1.values():
    print(x)
print(dict1.update(dict2))
print(dict1)"""