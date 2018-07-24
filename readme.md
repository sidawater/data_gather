  使用文档(草稿)
----

* ### 独立数据类型  `gather.SingleData(dict)`
 继承自 dict, 仅添加部分功能便于数据提取和处理

* ##### 数据初始化
```
Out[49]: single_data = SingleData({'num': 5, 'str': '5'})

In [50]: single_data.num
Out[50]: 5

In [51]: single_data.str
Out[51]: '5'
```

* ##### 支持类型转换, 现仅支持 `float`, `int`, `str`
```
In [52]: single_data.int__str
Out[52]: 5

In [53]: type(single_data.int__str)
Out[53]: int

```

----

* ### 数据集类型  `gather.DataGather(BaseDataGather)`
继承自 list, 添加搜索功能, 支持链式搜索

* #### 初始化
```
In [60]: data_list = [
    ...:     {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abc'},
    ...:     {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abt'},
    ...:     {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abegas'},
    ...:     {'uid': '02', 'type': 4, 'other': '63', 'desc': 'ab_start'},
    ...:     {'uid': '02', 'type': 4, 'other': '63', 'desc': 'abc'},
    ...:     {'uid': '02', 'type': 4, 'other': '63', 'desc': 'abffffff'},
    ...:     {'uid': '02', 'type': 15, 'other': 45, 'desc': 'abcccc'},
    ...:     {'uid': '02', 'type': 15, 'other': 45, 'desc': 'def'},
    ...:     {'uid': '02', 'type': 15, 'other': 45, 'desc': 'def'},
    ...:     {'uid': '03', 'type': 15, 'other': 12, 'desc': 'def'},
    ...:     {'uid': '03', 'type': 15, 'other': 12, 'desc': 'def'},
    ...:     {'uid': '03', 'type': 100, 'other': 12, 'desc': 'def'},
    ...:     {'uid': '04', 'type': 100, 'other': '3', 'desc': 'def'},
    ...:     {'uid': '04', 'type': 1, 'other': '2', 'desc': 'def'},
    ...:     {'uid': '04', 'type': 1, 'other': '6', 'desc': 'def'},
    ...: ]
    ...: data_list = [SingleData(data) for data in data_list]
    ...:
    ...: data_gather = DataGather(data_list)

```


* #### `gather.DataGather.filter(**kwargs)`

* ##### 支持条件搜索
```
In [74]: dg = data_gather.filter(uid='01')
    ...: dg.show()

Out[74]:
[{'uid': '01', 'type': 4, 'other': 63, 'desc': 'abc'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abt'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abegas'}]
```

* ##### 支持链式搜索
```
In [76]: dg = data_gather.filter(uid='01').filter(desc='abc')
    ...: dg.show()
    ...:
    ...:
Out[76]: [{'uid': '01', 'type': 4, 'other': 63, 'desc': 'abc'}]

```

* ##### 自动链式搜索 `data_gather.filter(uid='01')` 等同于 `dg = data_gather.uid('01')`
```
In [86]: dg = data_gather.uid('01')
    ...: dg.show()

Out[86]:
[{'uid': '01', 'type': 4, 'other': 63, 'desc': 'abc'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abt'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abegas'}]

```

* ##### 支持范围搜索 `data_gather.filter(uid='01')`

&nbsp; &nbsp; &nbsp;搜索字段后添加 `__gt`, 即可对应　'>'　运算

```
In [87]: dg = data_gather.filter(type__gt=4)
    ...: dg.show()

Out[87]:
[{'uid': '02', 'type': 15, 'other': 45, 'desc': 'abcccc'},
 {'uid': '02', 'type': 15, 'other': 45, 'desc': 'def'},
 {'uid': '02', 'type': 15, 'other': 45, 'desc': 'def'},
 {'uid': '03', 'type': 15, 'other': 12, 'desc': 'def'},
 {'uid': '03', 'type': 15, 'other': 12, 'desc': 'def'},
 {'uid': '03', 'type': 100, 'other': 12, 'desc': 'def'},
 {'uid': '04', 'type': 100, 'other': '3', 'desc': 'def'}]

```

&nbsp; &nbsp; &nbsp;同样支持其他逻辑运算
```
__is: is
__is_not: is not
__not: !=
__gt: >
__gte: >=
__lt: <
__lte: <=
```
&nbsp; &nbsp; &nbsp;举例
```
In [88]: dg = data_gather.filter(int__other__gte=45)
    ...: dg.show()

Out[88]:
[{'uid': '01', 'type': 4, 'other': 63, 'desc': 'abc'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abt'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abegas'},
 {'uid': '02', 'type': 4, 'other': '63', 'desc': 'ab_start'},
 {'uid': '02', 'type': 4, 'other': '63', 'desc': 'abc'},
 {'uid': '02', 'type': 4, 'other': '63', 'desc': 'abffffff'},
 {'uid': '02', 'type': 15, 'other': 45, 'desc': 'abcccc'},
 {'uid': '02', 'type': 15, 'other': 45, 'desc': 'def'},
 {'uid': '02', 'type': 15, 'other': 45, 'desc': 'def'}]

```

* ##### 支持正则搜索 `dg = data_gather.filter(desc__like='ab.*')`
使用python语法的正则
在使用字段后添加 `__like` 即可使用正则判断 (`re.search` 操作)
```
In [89]: dg = data_gather.filter(desc__like='ab.*')
    ...: dg.show()

Out[89]:
[{'uid': '01', 'type': 4, 'other': 63, 'desc': 'abc'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abt'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abegas'},
 {'uid': '02', 'type': 4, 'other': '63', 'desc': 'ab_start'},
 {'uid': '02', 'type': 4, 'other': '63', 'desc': 'abc'},
 {'uid': '02', 'type': 4, 'other': '63', 'desc': 'abffffff'},
 {'uid': '02', 'type': 15, 'other': 45, 'desc': 'abcccc'}]

```

* ##### 支持自定义函数搜索 `data_gather.filter(type__func={'func': func, 'params': 4})`
```
In [90]: def func(obj, key, par):
    ...:     return getattr(obj, key) > par
    ...:
    ...: dg = data_gather.filter(type__func={'func': func, 'params': 4})
    ...: dg.show()

Out[90]:
[{'uid': '02', 'type': 15, 'other': 45, 'desc': 'abcccc'},
 {'uid': '02', 'type': 15, 'other': 45, 'desc': 'def'},
 {'uid': '02', 'type': 15, 'other': 45, 'desc': 'def'},
 {'uid': '03', 'type': 15, 'other': 12, 'desc': 'def'},
 {'uid': '03', 'type': 15, 'other': 12, 'desc': 'def'},
 {'uid': '03', 'type': 100, 'other': 12, 'desc': 'def'},
 {'uid': '04', 'type': 100, 'other': '3', 'desc': 'def'}]

```
