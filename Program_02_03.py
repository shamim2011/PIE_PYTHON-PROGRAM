Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # tuple
>>> a=(23,45,56,78,43,56,12,34,23,233,45,22)
>>> a
(23, 45, 56, 78, 43, 56, 12, 34, 23, 233, 45, 22)
>>> a.index(12)
6
>>> a.count(23)
2
>>> 
>>> # dictionary
>>> a = {"aman":"oppo","manoj":"poco","ekta":"motorola"}
>>> a
{'aman': 'oppo', 'manoj': 'poco', 'ekta': 'motorola'}
>>> a.key()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.key()
AttributeError: 'dict' object has no attribute 'key'
>>> a.keys()
dict_keys(['aman', 'manoj', 'ekta'])
>>> a.values()
dict_values(['oppo', 'poco', 'motorola'])
>>> 
>>> 
>>> #set
>>> a={21,43,45,45,678,43,76,887};
>>> b = {21,34,56,78,89,32,56,87,32,87}
>>> a
{21, 678, 887, 43, 76, 45}
>>> b
{32, 34, 21, 87, 56, 89, 78}
>>> a.difference(b)
{678, 43, 76, 45, 887}
>>> b.difference(a)
{32, 34, 78, 87, 56, 89}
>>> a.intersection(b)
{21}
>>> a.union(b)
{32, 34, 678, 43, 76, 45, 78, 21, 87, 887, 56, 89}
>>> 