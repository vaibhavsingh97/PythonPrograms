# Write a program to create an ordered dictionary.

import collections

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'
print "D1 dictionary:"
for k, v in d1.items():
    print k, v
print "D2 dictionary:"
for k, v in d2.items():
    print k, v
print 'Regular dictionary:'
print d1 == d2, "\n"


d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'
print "D1 dictionary:"
for k, v in d1.items():
    print k, v
print "D2 dictionary:"
for k, v in d2.items():
    print k, v
print 'OrderedDict:'
print d1 == d2
