# -*- coding: UTF-8 -*-
# by sidawater


class BaseSingleData(dict):
    def __getattr__(self, key):
        return self.get(key)


class BaseDataGather(list):
    """
    used for chain filter
    """

    __created = False


    def __init__(self, src, chain_step=None, **kwargs):
        self._source = src
        self.__filter_conditions = kwargs
        self.__chain_step = chain_step

        if (not self.__chain_step) and (not self.__filter_conditions):
            self.__created = True
            self.extend([i for i in self._source])

    def __filter_judge(self, obj, **kwargs):
        for k, v in kwargs.items():
            if not self._judge(k, v, obj):
                return False
        return True

    def __getattr__(self, key):
        return type(self)(src=self._source, chain_step=key, **self.__filter_conditions)

    def __call__(self, value):
        return self.filter(**{self.__chain_step: value})

    def __create(self):
        if not self.__created:
            self._source = [i for i in self._source if self.__filter_judge(obj=i, **self.__filter_conditions)]
            self.extend(self._source)
            self.__filter_conditions = {}
            self.__created = True

    def filter(self, **kwargs):
        self.__filter_conditions.update(kwargs)
        return type(self)(self._source, **self.__filter_conditions)

    def _judge(self, key, value, obj):
        return self.judgments(key, value, obj)

    def judgments(self, key, value, obj):
        return obj_value == refer_value

    def show(self):
        self.__create()
        print(self)
        return self
