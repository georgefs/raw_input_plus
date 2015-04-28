#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

import time
import sys

class Field(object):
    default_validators = []
    description_format = '''
        {description}
    '''
    
    def __init__(self, description='', null=False, validators=[]):
        self._description = description
        self.null=null
        self.validators = validators

    @property
    def description(self):
        return self._description

    def raw_input(self, name="input"):
        print self.description_format.format(name=name, description=self.description)
        while True:
            _input = raw_input("{}:".format(name))
            if self.validator(_input):
                return self.to_data(_input)

    def _validators(self):
        return self.validators + self.default_validators

    def validator(self, value):
        for validator in self._validators:
            assert validator(value), 'error'
        return True
    
    def to_data(self, value):
        return value





class FieldSet(object):
    def raw_input(self):
        fields = [(f, getattr(self, f)) for f in dir(self) if isinstance(getattr(self, f), Field)]
        result = {}
        for name, field in fields:
            result[name] = field.raw_input(name)
        return result




