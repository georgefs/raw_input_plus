#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.


from raw_input_plus.fields import (
            ChoiceField, DateTimeField, EmailField,
            FileField, FloatField, IPAddressField,
            IntField, StringField
        )
from raw_input_plus import FieldSet
from mock import patch
import unittest


class FieldTest(unittest.TestCase): 
    def test_choice_field(self):
        with patch('__builtin__.raw_input') as mock_input:
            ## Sequence raw input 
            print raw_input
            mock_input.side_effect = ["a", "2", "b"]
            ## choice 
            choice = {
                "1": "test1",
                "2": "test2",
                "3": "test3"
            }
            result = ChoiceField(choice=choice).raw_input()
            self.assertEqual(result, "test2")
            self.assertEqual(mock_input.call_count, 2)


    def test_datetime_field(self):
        with patch('__builtin__.raw_input') as mock_input:
            ## Sequence raw input 
            from datetime import datetime
            now = datetime.now()
            time_format = "%Y-%m-%dT%H:%M:%S"

            now_str = now.strftime(time_format)
            target = datetime.strptime(now_str, time_format)

            mock_input.side_effect = ["test", now_str, "213"]

            result = DateTimeField(datetime_format=time_format).raw_input()
            self.assertEqual(result, target)
            self.assertEqual(mock_input.call_count, 2)



    def test_email_field(self):
        with patch('__builtin__.raw_input') as mock_input:
            ## Sequence raw input 
            target = "test@mail.com"
            mock_input.side_effect = ["test", target, "213"]

            result = EmailField().raw_input()
            self.assertEqual(result, target)
            self.assertEqual(mock_input.call_count, 2)



    def test_ip_field(self):
        with patch('__builtin__.raw_input') as mock_input:
            ## Sequence raw input 
            target = "127.0.0.1"
            mock_input.side_effect = ["test", target, "213"]

            result = IPAddressField().raw_input()
            self.assertEqual(result, target)
            self.assertEqual(mock_input.call_count, 2)



    def test_file_field(self):
        with patch('__builtin__.raw_input') as mock_input:
            ## Sequence raw input 
            curr = __file__
            mock_input.side_effect = ["tessasdaddt", curr, "teadsd"]

            result = FileField().raw_input()
            self.assertEqual(mock_input.call_count, 2)


    def test_int_field(self):
        with patch('__builtin__.raw_input') as mock_input:
            ## Sequence raw input 
            curr = "1234"
            mock_input.side_effect = ["tessasdaddt", curr, "teadsd"]

            result = IntField().raw_input()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(int(curr), result)


    def test_float_field(self):
        with patch('__builtin__.raw_input') as mock_input:
            ## Sequence raw input 
            curr = "123.4"
            mock_input.side_effect = ["tessasdaddt", curr, "teadsd"]

            result = FloatField().raw_input()
            self.assertEqual(mock_input.call_count, 2)
            self.assertEqual(result, float(curr))



    def test_string_field(self):
        with patch('__builtin__.raw_input') as mock_input:
            ## Sequence raw input 
            target = "test"
            mock_input.side_effect = [target, "tasdasd", "teadsd"]
            result = StringField().raw_input()
            self.assertEqual(mock_input.call_count, 1)
