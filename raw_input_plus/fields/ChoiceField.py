#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.


from raw_input_plus.base import Field
import re

class ChoiceField(Field):
    default_validators = []
    ## key need string
    def __init__(self, choice=None, validators=[], *args, **kwargs):
        assert choice, 'error not set '
        self.choice = choice
        
        validators.append(lambda v:v in [k for k in choice.keys()])
            
        kwargs.update({"validators": validators})

        options_str = ["{} : {}".format(name, value) for name, value in choice.items()]
        options_str = "\n".join(options_str)
        
        self.default_description = '''
            choice input
            \n{}
        '''.format(options_str)

        return super(ChoiceField, self).__init__(*args, **kwargs)
    
    def to_data(self, value):
        return self.choice.get(value)
        

