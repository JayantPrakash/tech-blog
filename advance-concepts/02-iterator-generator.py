"""
An iterator is an object that can be iterated using a loop. They give us one element at a time.
An iterator object must implement 2 methods, __iter__() and __next__().
Most python data structures e.g. lists, tuples, strings, sets are iterable.

We can also use iter() and next() in place of __iter__() and __next__(). 
These are just a more elegant way to call the methods.
Below is an example using a list.
"""

price = [210,300,400,500]

price_iter = price.__iter__()

print(price_iter.__next__())
print(price_iter.__next__())
print(price_iter.__next__())

# Output:
# 210
# 300
# 400
while True:
    try:
        print(price_iter.__next__())
    except StopIteration:
        break
    
"""
You might have observed that only a single element is printed, This is because python internally manages 
the state of the iterator and remembers up to which element, traversal is complete.
The main advantage of using iterators is that they save resources.  If we try to create a list of infinite natural numbers, 
It will lead to an overflow of our RAM memory and our program will break. However, It is theoretically possible using an Iterator.
"""    
class NaturalNumbers:
    """Infinite iterator to return natural numbers"""
    
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


value = iter(NaturalNumbers())
print(next(value))
print(next(value))
print(next(value))
print(next(value))

# Output:
# 1
# 2 
# 3
# 4

"""Generators"""

"""We do not want to create the iter method or the next method and directly want to use the concept of Iterators.
For this purpose, we will be moving on with generators. Generators are an elegant way to create iterators! 
Let's review a generator. Below is an example of a normal function that returns the number 10."""

def return_10():
    return 10

value = return_10()
print(value)

#Output: 10

"""As soon as a function returns something. The function is thrown away from the call stack of RAM 
and its lifespan is over. However, to use a generator, we use yield keyword 
which keeps the function alive and also maintains the state of the generator 
i.e. It also remembers the last yielded element."""
def return_values():
    yield 1
    yield 2
    yield "a"
    yield "b"


value = return_values()
print(value.__next__())
print(value.__next__())
print(next(value))

# Output : 
# 1
# 2
# a

"""We can also generate infinite natural numbers as before. Below is a generator program for that. 
I am going to restrict the numbers up to 99 however, we can generate as many as we want!"""

def InfiniteNaturals():
    start = 1

    while start < 100:
        yield start
        start += 1

numbers = InfiniteNaturals()
for item in numbers:
    print(item)

# Output
# 1
# 2
# ...
# 99