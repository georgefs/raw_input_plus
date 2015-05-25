#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus.base import Field
import re
import numbers

class IntField(Field):
    default_validators = [lambda v:re.match("^-?\d+$", v)]
    default_description = '''
        integer
    '''
    def __init__(self, max_number=None, min_number=None, validators=None, *args, **kwargs):
        validators = validators or []
        if isinstance(max_number, numbers.Number):
            validators.append(lambda v:int(v)<=max_number)

        if isinstance(min_number, numbers.Number):
            validators.append(lambda v:int(v)>=min_number)
        
        kwargs.update({'validators': validators})
        return super(IntField, self).__init__(*args, **kwargs)

    def to_data(self, value):
        return int(value)
