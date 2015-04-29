import os
from raw_input_plus.base import Field

def check_file_exist(value):
    if not os.path.isfile(value):
        return False
    else:
        return True

class FileField(Field):
    default_description = '''
        file
    '''
    default_validators = [check_file_exist]

    def to_data(self, value):
        return open(value)
