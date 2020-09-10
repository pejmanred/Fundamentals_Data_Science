import numpy as np
# FOR LOOP
for i in [10, 20, 30, 40, 50]:
    print ("Initial i is: ",i)                                 # first line in "for i" block
    for j in [10, 20, 30, 40, 50]:
        print( "j is: ", j)                         # first line in "for j" block
        print ("i+j: ",i+ j)                     # last line in "for j" block
        print("------------------")
    print ("i is getting updated: ",i)                                 # last line in "for i" block
print("done looping")

#LISTs

int_list = [1, 2, 3,4,5]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ int_list, heterogeneous_list, [] ]

list_length = len(int_list)     # equals 5
list_sum = sum(int_list)        # equals 15

#Get list elements
x = np.arange(20) 
zero = x[0] # equals 0, lists are 0-indexed
one = x[1] # equals 1
nineteenth = x[-1] #  last element
eighteenth = x[-2] #  next-to-last element
x[0] = -1 # now x is [-1, 1, 2, 3, ..., 19]

#Sliceing
first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [17, 18, 19]
without_first_and_last = x[1:-1] # [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,18]
copy_of_x = x[:]

x, y, z = [1, 2, 3] # now x is 1, y is 2, z is 3
_, y, z = [10, 20, 30] # now y == 20 and z == 30, didn't care about the first element

#TUPLES
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3 # my_list is now [1, 3]
try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")
    
def sum_and_product(x, y):
    return (x + y),(x * y)
sp = sum_and_product(2, 3) # equals (5, 6)
s, p = sum_and_product(5, 10) # s is 15, p is 50  

#Dictionaries
 empty = {}
 
 food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
 food["spam"] = "yes"
 
w={"house":"Haus","cat":"Katze","red":"rot"}
w.items()
w.keys()
w.values() 

from collections import Counter
c = Counter([0, 1, 2, 0,1,5,1])  #Counter({0: 2, 1: 3, 2: 1, 5: 1})

#Sets 
s = set()
s.add(1) # s is now { 1 }
s.add(2) # s is now { 1, 2 }
s.add(2) # s is still { 1, 2 }
x = len(s) # equals 2
y = 2 in s # equals True
z = 3 in s # equals False

'''
stopwords_list = ["a","an","at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list                         # False, but have to check every element
stopwords_set = set(stopwords_list)
"zip" in stopwords_set                          # very fast to check
'''

#The second reason is to find the distinct items in a collection:
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6
item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set) # [1, 2, 3]

#List Comprehensions
even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares = [x * x for x in range(5)]                 # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers] # [0, 4, 16]

me=list([[1,2,3,4],
         [10,20,30,40],
         [15,25 ,35, 45],
         [100,200,300,400]])  
import numpy as np   
story = [np.mean([x[i] for x in me]) for i in range(4)] #Average of each column [31.5, 61.75, 92.0, 122.25]

square_dict = { x : x * x for x in range(5) } # { 0:0, 1:1, 2:4, 3:9, 4:16 }
square_set = { x * x for x in [1, -1] } # { 1 }

zeroes = [0 for _ in even_numbers] # has the same length as even_numbers

pairs = [(x, y) for x in range(10) for y in range(10)] 

#Randomness
import random
six_uniform_randoms = [random.random() for _ in range(6)]

random.randrange(50) # choose randomly from range(10) = [0, 1, ..., 50]
random.randrange(3, 6) # choose randomly from range(3, 6) = [3, 4, 5]

up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten


lottery_numbers = range(100)
winning_numbers = random.sample(lottery_numbers, 8) # [13, 80, 35, 44, 21, 10, 0, 46] without replacement

fiver_with_replacement = [random.choice(range(20)) for _ in range(5)]

def double(x):
return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
twice_xs = map(double, xs) # same as above
list_doubler = partial(map, double) # *function* that doubles a list
twice_xs = list_doubler(xs) # again [2, 4, 6, 8]


def is_even(x):
"""True if x is even, False if x is odd"""
return x % 2 == 0
x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs) # same as above
list_evener = partial(filter, is_even) # *function* that filters a list
x_evens = list_evener(xs) # again [2, 4]
    