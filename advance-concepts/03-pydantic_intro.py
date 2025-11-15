"""
1.Pydantic is useful for data validation and type hints."""
from pydantic import BaseModel
from typing import Optional
class Blog(BaseModel):
    title: str 
    is_active: bool

Blog(title="My First Blog",is_active=True)

#Blog(title='Second One',is_active='yup!')

from pydantic import BaseModel

class Blog(BaseModel):
    title: str 
    description: Optional[str]=None
    is_active: bool

print(Blog(title="My First Blog",is_active=True))
# Output : Blog(title='My First Blog', description=None, is_active=True)
blog = Blog(title="My First Blog",is_active=True)
print(blog.dict())
print(blog.title)

""" 
2.Accepting only a subset of strings.
It's a very common scenario. Many times what we want is to allow only a subset of strings.
Let's say our Blog class has a property named language. Since, we only allow blogs on Java, Python, and Go. 
We want to restrict to only these 3 strings. We can accomplish this as follow."""

from pydantic import BaseModel
from enum import Enum

class Languages(str,Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"

class Blog(BaseModel):
    title: str 
    language : Languages = Languages.PY
    is_active: bool
    

blog = Blog(title="My First Blog",language="Java",is_active=True)
print(blog.language)
# Output: Blog(title='My First Blog', language=<Languages.JAVA: 'Java'>, is_active=True)

#print(Blog(title="My First Blog",language="C++",is_active=True))
# Output: ValidationError: 1 validation error for Blog language value is not a valid enumeration member; permitted: 'Python', 'Java', 'Go' 

"""
3.Getting dynamic values at runtime
To tackle such scenarios Pydantic provides us with a default_factory argument on a Field function.
"""

import time
from pydantic import BaseModel,Field
from datetime import datetime

class Blog(BaseModel):
    title: str 
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool

print(Blog(title="Our First Blog",is_active=True))
time.sleep(1)
print(Blog(title="Our Second Blog",is_active=True))

#Output: 
#title='...' created_at=datetime.datetime(2022, 10, 7, 15, 57, 46, 257846) is_active=True
#title='...' created_at=datetime.datetime(2022, 10, 7, 15, 57, 49, 261350) is_active=True

"""
4. Properties as Pydantic Models
We can actually have a nested pydantic model. I mean to say, we can use Pydantic models as fields
and can have sub-objects! Say, we updated our blog to have a comment system. 
In this case, we can have a property named comment which itself can be a Pydantic class."""

from pydantic import BaseModel
from typing import List

class Comment(BaseModel):
    text: Optional[str]=None

class Blog(BaseModel):
    title: str 
    comment: Optional[List[Comment]]
    is_active: bool

print(Blog(title="Our First Blog",comment=[{'text':'My comment'},{'text':'Your comment'},],is_active=True))

#Output: title='Our First Blog' comment=[Comment(text='My comment'), Comment(text='Your comment')] is_active=True