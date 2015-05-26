#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus.base import Field

class BoolField(Field):
    #default_validators = [lambda x: x=='0' or x=='1']
    default_validators = []
    default_description = '''
        0 : true
        1 : false
    '''

    def __init__(self, validators=None, *args, **kwargs):
        
        return super(BoolField, self).__init__(*args, **kwargs)

    def to_data(self, value):
        if value == '0':
            return "true"
        elif value == '1':
            return "false"
        raise Exception('error')
        
