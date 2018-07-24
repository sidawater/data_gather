import re
from .base import BaseDataGather, BaseSingleData
from ._tools import run_create


class SingleData(BaseSingleData):
    def __getattr__(self, key):
        if type(key) != str:
            return self.get(key)
        if key.startswith('int__'):
            return int(self.get(key.replace('int__', '')))
        elif key.startswith('float__'):
            return float(self.get(key.replace('float__', '')))
        elif key.startswith('str__'):
            return str(self.get(key.replace('str__', '')))
        else:
            return self.get(key)


class DataGather(BaseDataGather):

    @run_create
    def choice_random(self, rate):
        """
        return an instance of DataGather, which has (self.length * rage) samples of self._source
        """
        return type(self)(random.sample(self, int(self.length * rate + 0.5)))

    def judgments(self, key, value, obj):
        """
        rebuild filter conditions rules
        __is: is
        __is_not: is not
        __not: !=
        __gt: >
        __gte: >=
        __lt: <
        __lte: <=
        __like: re.search(rgx, value)
        __func: value like {'func': func, 'params': 'standard_value'}, func return True or False
        """

        if key.endswith('__is'):
            standard = getattr(obj, key.replace('__is', ''))
            return standard is value
        elif key.endswith('__is_not'):
            standard = getattr(obj, key.replace('__is_not', ''))
            return standard is not value
        elif key.endswith('__not'):
            standard = getattr(obj, key.replace('__not', ''))
            return standard != value

        elif key.endswith('__gt'):
            standard = getattr(obj, key.replace('__gt', ''))
            return standard > value
        elif key.endswith('__gte'):
            standard = getattr(obj, key.replace('__gte', ''))
            return standard >= value
        elif key.endswith('__lt'):
            standard = getattr(obj, key.replace('__lt', ''))
            return standard < value
        elif key.endswith('__lte'):
            standard = getattr(obj, key.replace('__lte', ''))
            return standard <= value
        elif key.endswith('__like'):
            standard = getattr(obj, key.replace('__like', ''))
            rgx = re.compile(value)
            return re.search(rgx, standard)
        elif key.endswith('__func'):
            return value['func'](obj, key.replace('__func', ''), value.get('params'))
        else:
            standard = getattr(obj, key)
            return standard == value
