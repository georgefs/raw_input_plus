#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.


from raw_input_plus.base import Field
import re
import collections

class ChoiceField(Field):
    default_validators = []
    ## key need string
    def __init__(self, choice=None, validators=None, *args, **kwargs):

        if isinstance(choice, (list, tuple)):
            count = 0
            choice = dict((str(idx), choice[idx]) for idx in range(len(choice)) )

        validators = validators or []
        assert choice, 'error not set '
        self.choice = choice
        
        validators.append(lambda v:v in [k for k in choice.keys() + choice.values()])
            
        kwargs.update({"validators": validators})

        options_str = ["{} : {}".format(name, value) for name, value in choice.items()]
        options_str = "\n".join(options_str)
        
        self.default_description = '''
            choice input
            \n{}
        '''.format(options_str)

        return super(ChoiceField, self).__init__(*args, **kwargs)
    
    def to_data(self, value):
        if self.choice.has_key(value):
            return self.choice.get(value)
        elif value in self.choice.values():
            return value
        raise Exception('error')

