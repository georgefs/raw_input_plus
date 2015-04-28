#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

class Field(object):
    default_validators = []
    
    def __init__(self, description='', choice=None, null=False):
        self._description = description
        self.choice=choice
        self.null=null

    @property
    def description(self):
        return self._description

    def raw_input(self):
        while True:
            _input = raw_input(self.description)
            if self.validator(_input):
                return self.to_data(_input)

    def validator(self, value):
        return True
    
    def to_data(self, value):
        return value





class FieldSet(object):

    def raw_input(self):
        fields = [(f, getattr(self, f)) for f in dir(self) if isinstance(getattr(self, f), Field)]
        result = {}
        for name, field in fields:
            result[name] = field.raw_input()
        return result



class UserFieldSet(FieldSet):
    name = Field(description="name:")
    age = Field(description="age:")




print UserFieldSet().raw_input()
