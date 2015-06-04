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

    def __init__(self, description='', validators=None, *args, **kwargs):

        self.default_description = description + "\n\t0 : true\n\t1 : false\t"

        return super(BoolField, self).__init__(*args, **kwargs)

    def to_data(self, value):
        if value == '0':
            return "boolTrue"
        elif value == '1':
            return "boolFalse"
        raise Exception('error')
        
