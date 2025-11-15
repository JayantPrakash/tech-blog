"""Data Validation
we don't want the title to be less than 5 characters in length. This can be done as follow:
min_length is just one of the available hooks, To know of more of the hooks see hooks for str, hooks for int, hooks for list. There are many more hooks e.g.

gt: int = None: enforces integer to be greater than the set value
multiple_of: int = None: enforces integer to be a multiple of the set value
strip_whitespace: bool = False: removes leading and trailing whitespace
regex: str = None: regex to validate the string against
"""

from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(min_length=5)
    is_active: bool

print(Blog(title="height",is_active=False))
# Output: ValidationError: 1 validation error for Blog title
# ensure this value has at least 5 characters

"""Validation with Custom Hooks
In real-world projects and products, these validations are rarely sufficient. 
Say, we want to validate the title. If the title contains 'delete from' substring, 
We want to raise a ValueError. We can achieve this as follow:"""

from pydantic import BaseModel,Field, validator

class Blog(BaseModel):
    title: str = Field(...,min_length=5)
    is_active: bool

    @validator("title")
    def validate_no_sql_injection(cls, value):
        if "delete from" in value:
            raise ValueError("Our terms strictly prohibit SQLInjection Attacks")
        return value

print(Blog(title="delete",is_active=True))
# Output: ValidationError: 1 validation error for Blog title
# Our terms strictly prohibit SQLInjection Attacks

"""Validating interdependent properties with custom hooks
Many times, one property is dependent on another property of the class.
Say, we require the users to send their email, password, and confirm_password for registration. 
It is evident that we need to check if the password has the same value as that of confirm_password. 
In such cases, single field validation will not suffice. Pydantic provides a root_validator decorator 
which helps to tackle such cases."""

from pydantic import BaseModel, root_validator

class CreateUser(BaseModel):
    email : str
    password :str 
    confirm_password :str 

    @root_validator()
    def verify_password_match(cls,values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise ValueError("The two passwords did not match.")
        return values

print(CreateUser(email="ping@fastapitutorial.com",password="123",confirm_password="123"))

# Output: ValidationError: 1 validation error for CreateUser __root__
#  The two passwords did not match. (type=value_error)