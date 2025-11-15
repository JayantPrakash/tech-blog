
"""Annotating with simple data types"""

count = 5
print(type(count))

count = '5'
print(type(count))

def total_price(price_1,price_2):
    return f"Your total bill is USD {price_1+price_2}"
        
print(total_price(30,40))

def total_price(price_1,price_2):
    return f"Your total bill is USD {price_1+price_2}"
        
print(total_price('30','40'))


def total_price(price_1:int,price_2:int):
    return f"Your total bill is USD {price_1+price_2}"
        
price = total_price('30','40')
print(price)    

"""Annotating with simple data structures."""

# For python version <=3.9
from typing import List, Tuple, Dict 


price: List[int] = [213,234,984]
immutable_price: Tuple[int,int,int] = (231,983,704)
price_dict: Dict[str,int] = {
    'item_1' : 340,
    'item_2' : 500,
}

# In the above snippet, we saw, how to annotate with a type of basic data structure. 
# However, this is valid for Python 3.9 and lower. 
# In the newer versions of Python, we can directly use the list, tuple, and dict keywords.

new_price: list[int] = [14,902,898]
new_immutable_price: tuple[int,int,int] = (388,392,299)
new_price_dict: dict[str,int] = {
    "item_1":240,
    "item_2":490,
}

"""Annotating with complex data structures."""


from typing import Union

x: List[Union[int,float]] = [2,3,4.1,5,6.2]

x: List[int|float] = [2,3,4.1,5,6.2]  #newer syntax in python 3.10+

def inr_to_usd(value:float) -> Union[float,None]:
    try:
        conversion_factor = 75
        value = value/conversion_factor
        return value
    except TypeError:
        return None

print(inr_to_usd(23))

"""Custom Types:
If your type hints are becoming too lengthy, then it becomes very difficult to read and understand the function.
In such cases, we can extract the type annotation and build our own custom type. Let's see an example of this."""

from typing import List 

Image = List[List[int]]

def flatten_image(image: Image)->List:  #custom type Image
    flat_list = []
    for sublist in image:
        for item in sublist:
            flat_list.append(item)
    return flat_list

image = [[1,2,3],[4,5,6]]
print(flatten_image(image))

"""we can type annotate our custom classes"""

from typing import Optional

class Job:
    def __init__(self,title:str,description:Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return self.title


job1 = Job(title="SDE2",description="Sdfdk")
job2 = Job(title="Senior Manager", description="jfjdj")

jobs: List[Job] = [job1,job2]     #notice the List[Job] , Job is our custom class

print(jobs)

"""Annotate functions with callables

A decorator is basically a function that wraps another function 
and adds additional functionality to it. This is similar to packing a gift.
The decorator acts as a wrapper. Below, we have a simple divide function but,
division by 0 is not practical. What we can do is decorate the divide function 
with another function that can handle the edge case of division by 0."""

def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(9, 0)

"""If we want to annotate the func parameter then we can make use of the Callable class.
This will help other developers understand the signature of the func parameter."""
from typing import Callable

def smart_divide(func:Callable[[int,int],float]):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)
    return inner

@smart_divide
def divide(a:int, b:int)->float|None:
    print(a/b)

divide(9, 0)