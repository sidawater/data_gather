# -*- coding: UTF-8 -*-
# by sidawater
from ._tools import run_create


class BaseSingleData(dict):
    def __getattr__(self, key):
        return self.get(key)


class BaseDataGather(list):
    """
    used for chain filter
    main function is filter and chain filter
    e.g.
        bdg = BaseDataGather([obj1, obj2..])
        `x = bdg.filter(column1=value1, column2=value2).filter(column3=value3)`
        or
        x = bgd.column1(value1).column2(value2)
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

    def _create(self):
        if not self.__created:
            self._source = [i for i in self._source if self.__filter_judge(obj=i, **self.__filter_conditions)]
            self.extend(self._source)
            self.__filter_conditions = {}
            self.__created = True

    def filter(self, **kwargs):
        kwargs.update(self.__filter_conditions)
        return type(self)(self._source, **kwargs)

    def _judge(self, key, value, obj):
        x = self.judgments(key, value, obj)
        return x

    def judgments(self, key, value, obj):
        return getattr(obj, key) == value

    # def append(self, value):
    #     if self.__created:
    #         self.append(value)
    #     self._source.append(value)
    #
    # def extend(self, value_list):
    #     if self.__created:
    #         self.extend(value_list)
    #     self._source.extend(value)

    @run_create
    def show(self):
        return self

    @property
    @run_create
    def length(self):
        return len(self)
