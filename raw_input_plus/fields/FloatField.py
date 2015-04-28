#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus.base import Field

import re

class FloatField(Field):
    default_validators = [lambda v:re.match("^\d+(.\d+)?$", v)]
    default_description = " float "
    def __init__(self, max_number=None, min_number=None, validators=[], *args, **kwargs):
        if isinstance(max_number, float):
            validators.append(lambda v:float(v)<=max_number)

        if isinstance(min_number, float):
            validators.append(lambda v:float(v)>=max_number)

        return super(FloatField, self).__init__(*args, **kwargs)

    def to_data(self, value):
        return int(value)

