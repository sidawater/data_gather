import random
from .base import BaseDataGather, BaseSingleData


class SingleData(BaseSingleData):
    def __getattr__(self, key):
        if type(key) != str:
            return self.get(key)
        if key.startswith('int__'):
            return int(self.get(key.replace('int__'))
        elif key.startswith('float__'):
            return float(self.get(key.replace('float__'))
        elif key.startswith('str__'):
            return str(self.get(key.replace('str__'))


class DataGather(BaseDataGather):

    def choice_random(self):
        pass

    def judgments(self, key, value, obj):

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
        else:
            standard = getattr(obj, key)
            return standard == value
