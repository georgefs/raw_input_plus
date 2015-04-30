README
===

This is a tool which helps you on command line input.  
When doing command line input, we often need to type a lot of parameters, and those are fixed and even hard to remember.  
In raw_input_plus, we define some fields which user can utilize easily.  

##Installation

```
git clone https://github.com/georgefs/raw_input_plus.git
cd raw_input_plus
python setup.py install
```

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

```python
from raw_input_plus.base import Field
from raw_input_plus.fields import *

password = StringField(max_length=8, min_length=2, regexp=r'[\d]+')
print password.raw_input()
```

- Int

```python
from raw_input_plus.base import Field
from raw_input_plus.fields import *

magic_number = IntField(max_number=255, min_number=0)
print magic_number.raw_input()
```

- Choice

```python
from raw_input_plus.base import Field
from raw_input_plus.fields import *

ch = [('chocolate', 130), ('strawberry', 120)]
cake_selection = ChoiceField(choice=ch)
print cake_selection.raw_input()
```

- DateTime

```python
from raw_input_plus.base import Field
from raw_input_plus.fields import *

# you can specify datetime format, start_time and even end_time
birthday = DateTimeField(datetime_format="%Y-%m", start_time=datetime(1995, 1, 1), end_time=datetime.now())
print birthday.raw_input()
```

- Email

```python
from raw_input_plus.base import Field
from raw_input_plus.fields import *

your_mail = EmailField()
print your_mail.raw_input()
```

- File

```python
from raw_input_plus.base import Field
from raw_input_plus.fields import *

your_file = FileField()
print your_file.raw_input()
```

- Float

```python
from raw_input_plus.base import Field
from raw_input_plus.fields import *

magic_float = IntField(max_number=13.49, min_number=0.5)
print magic_float.raw_input()
```

- IPAddress

```python
from raw_input_plus.base import Field
from raw_input_plus.fields import *

magic_IP = IPAddressField()
print magic_IP.raw_input()
```

