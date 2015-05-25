from raw_input_plus.base import Field
from datetime import datetime


class DateTimeField(Field):
    default_validators = []

    def __init__(self, datetime_format="%Y-%m-%d", validators=None, start_time=None, end_time=None, *args, **kwargs):
        validators = validators or []

        self.datetime_format = datetime_format
        if isinstance(start_time, datetime):
            validators.append(lambda x: self.to_data(x) >= start_time)
        if isinstance(end_time, datetime):
            validators.append(lambda x: self.to_data(x) <= end_time)
        self.default_description = " \n\tdatetime, format: " + self.datetime_format + ", \n"
        if start_time:
            self.default_description += "\tstarting from " + str(start_time) + "\n"
        if end_time:
            self.default_description += "\tand ends from " + str(end_time) + "\n"

        validators.append(lambda x: isinstance(datetime.strptime(x, self.datetime_format), datetime))

        kwargs.update({"validators": validators})
        super(DateTimeField, self).__init__(*args, **kwargs)

    def to_data(self, value):
        dt = datetime.strptime(value, self.datetime_format)
        return dt
    
   

