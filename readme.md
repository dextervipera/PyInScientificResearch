# lab01

## updates

1. conda update conda
2. conda update anaconda

## enviroments

conda info -e --envs
conda create -n NAME ipython(packages)
conda activate -n NAME
conda env remove -n NAME

## ipython magic finction

%pwd

# data generation

## list

1. range() - obiekt iteratora liczb *int* z okre�lonego zakresu
1.1 list(range(10))
1.2 range(start, stop, step)
2. list comprehension

## tuple
	
simple text

# @ Anaconda Powershell promppt


## Formatowanie stringów


### format()

```
    'name: {}'.format(54)
```

```
s1 = 'nameL {}, age: {}'
s1.format('Jon', 23)
```

```
s2 = 'name: {2}, age (1:2f)'
s2.foramt(23, 'Join')
```

```
l2 = [24, 'Jon']
s2.format(*l1)
```

```
s3 = "name: {:<5}, age: {}"
print(s3.format(*l1))
```


```
s = 'pole1: {:<10}, pole2: {:=10}, pole3: {:>2f}'

In [20]: s = 'pole1: {:<10}, pole2: {:<10}, pole3: {:.2f}'

In [21]: s.format('aa', 'bb', 23.2412)
Out[21]: 'pole1: aa        , pole2: bb        , pole3: 23.24'

In [22]: s = 'pole1: {:<10},\npole2: {:<10},\npole3: {:.2f}'

In [23]: s.format('aa', 'bb', 23.2412)
Out[23]: 'pole1: aa        ,\npole2: bb        ,\npole3: 23.24'

In [24]: print(s.format('aa','bb',2432.4356426)
    ...: )
pole1: aa        ,
pole2: bb        ,
pole3: 2432.44

In [25]: arg = ('gds','asdg',2143645/2532)

In [26]: print(s.format(*arg))
pole1: gds       ,
pole2: asdg      ,
pole3: 846.62

In [27]: print(s.format(arg))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [27], in <cell line: 1>()
----> 1 print(s.format(arg))

TypeError: unsupported format string passed to tuple.__format__

In [28]: print(s.format(*arg))
pole1: gds       ,
pole2: asdg      ,
pole3: 846.62

In [29]:
```

### dictionary

```
In [38]: edudict.keys()
Out[38]: dict_keys([1, 2, 3])

In [39]: list(edudict.keys())[-1]
Out[39]: 3

In [40]: edudict.items()
Out[40]: dict_items([(1, '1'), (2, '2'), (3, '3')])

In [41]: list(edudict.items())
Out[41]: [(1, '1'), (2, '2'), (3, '3')]

In [42]: object=edudict.items()

In [43]: obj=edudict.items()

In [44]: list(obj)[-2]
Out[44]: (2, '2')

In [45]: print(object)
dict_items([(1, '1'), (2, '2'), (3, '3')])

In [46]: keys = [0,1,2]

In [47]: vals = ['q','w','e']
```

#### Zip -> dictionary
```
In [5]: keys = [0,1,2]

In [6]: vals = ['q','w','e']

In [7]: edidict = dict(zip(keys,vals))

In [8]: print(edidict)
{0: 'q', 1: 'w', 2: 'e'}
```

### List-in-list
```
In [1]: l1 = ['Adamn', []]

In [2]: l2 = ['no', 156, 'asdg']

In [3]: l1[1] = l2

In [4]: print(l1)
['Adamn', ['no', 156, 'asdg']]

In [5]: l1[1] = l2[:]

In [6]: l1[1][1] = ['Cezary nosi okulary'. 'Doktor Okulista']
  Input In [6]
    l1[1][1] = ['Cezary nosi okulary'. 'Doktor Okulista']
                                       ^
SyntaxError: invalid syntax


In [7]: l1[1][1] = ['Cezary nosi okulary', 'Doktor Okulista']

In [8]: print(l1)
['Adamn', ['no', ['Cezary nosi okulary', 'Doktor Okulista'], 'asdg']]
```

### even more sophosticated
```
In [10]: print(l1)
[3, 2, 3, ['fds', '325623']]

In [11]: l1[1] = {1:4, 5:6, 7:'asgdas'}

In [12]: print(l1)
[3, {1: 4, 5: 6, 7: 'asgdas'}, 3, ['fds', '325623']]
```

### Zadanie: model bazy danych imię:nazwisko, telefon, wzrost, cos w oparciu o listę i słwnik
keys = ['name'  , 'sname', 'phone', 'height', 'sth']
val1 = ['Barbie', 'adaws', 643463 , 1.84    , '??']
val2 = ['Ken'   . 'Berka', 195649 , 1.45    , "M"]
base = [dict(zip(keys,val1)), dict(zip(keys,val2))]


### Merging lists
```
In [40]: lsht = list(range(1,10))

In [41]: lsht
Out[41]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

In [42]: lsht.append(325)

In [43]: print(lsht)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 325]

In [44]: s_lsht = [325,2641,44]

In [45]: lsht.append(s_lsht)

In [46]: print(lsht)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 325, [325, 2641, 44]]

In [47]: lsht.extend(s_lsht)

In [48]: print(lsht)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 325, [325, 2641, 44], 325, 2641, 44]
111

```

.pop(n)
.remove(value)

# loops

## for loop
```
In [66]: sl = dict(zip([1,2,3],
    ...: ['a','b','c']))

In [67]: for ite in sl:
    ...:     print(ite)
    ...:
1
2
3
```

```
In [68]: for ite in sl.keys():
    ...:     print(ite)
    ...:
1
2
3
```

```
In [69]: for ite in sl.items():
    ...:     print(ite)
    ...:
(1, 'a')
(2, 'b')
(3, 'c')
```

```
In [70]: for k,v in sl.items():
    ...:     print(k,v)
    ...:
1 a
2 b
3 c
```

## Lista skłądana - list comprehension

### List comprehension
```
[x**2 for x in range(5)]
```


### dictionary comprehension
```
In [80]: dd = {k:v**3 for k,v in {'a':5, 'b':3}.items()}

In [81]: print(dd)
{'a': 125, 'b': 27}
```