README
===

This is a tool which helps you on command line input.  
When doing command line input, we often need to type a lot of parameters, and those are fixed and even hard to remember.  
In raw_input_plus, we define some fields which user can utilize easily.  

##Usage

you can put your own description or just use the deafult ones.


```python
from raw_input_plus.base import FieldSet
from raw_input_plus.fields import *
from datetime import datetime

class UserFieldSet(FieldSet):
    name = StringField(description="your name")
    # you can specify datetime format, start_time and even end_time
    birthday = DateTimeField(datetime_format="%Y-%m", end_time=datetime.now())
    mail = EmailField()

print UserFieldSet().raw_input()

```

##Fields

- String
- Int
- Choice
- DateTime
- Email
- File
- Float
- IPAddress
