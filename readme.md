
```
In [84]: data_list = [
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

```
In [85]: dg = data_gather.filter(uid='01')
    ...: dg.show()

Out[85]:
[{'uid': '01', 'type': 4, 'other': 63, 'desc': 'abc'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abt'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abegas'}]
```

```
In [86]: dg = data_gather.uid('01')
    ...: dg.show()

Out[86]:
[{'uid': '01', 'type': 4, 'other': 63, 'desc': 'abc'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abt'},
 {'uid': '01', 'type': 4, 'other': 63, 'desc': 'abegas'}]

```

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
