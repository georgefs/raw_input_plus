#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.

from raw_input_plus.base import Field

import re

import numbers

class FloatField(Field):
    default_validators = [lambda v:re.match("^-?\d+(.\d+)?$", v)]
    default_description = " float "
    def __init__(self, max_number=None, min_number=None, validators=None, *args, **kwargs):
        validators = validators or []
        if isinstance(max_number, numbers.Number):
            validators.append(lambda v:float(v)<=max_number)

        if isinstance(min_number, numbers.Number):
            validators.append(lambda v:float(v)>=min_number)

        kwargs.update({"validators": validators})

        return super(FloatField, self).__init__(*args, **kwargs)

    def to_data(self, value):
        return float(value)

