#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.


from raw_input_plus.base import Field
import re

class StringField(Field):
    default_validators = []
    default_description = " string "
    def __init__(self, max_length=None, min_length=None, regexp=None, validators=None, *args, **kwargs):
        validators = validators or []
        if isinstance(max_length, int):
            validators.append(lambda v:len(v) <= max_length)

        if isinstance(min_length, int):
            validators.append(lambda v:len(v) >= min_length)

        if isinstance(regexp, basestring):
            validators.append(lambda v:re.match(regexp, v))
        
        kwargs.update({"validators": validators})
        return super(StringField, self).__init__(*args, **kwargs)


