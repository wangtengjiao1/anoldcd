# -*- coding: utf-8 -*-
# __author__ = 'neo'
# __name__ = '王腾蛟'
# __time__ = '2015年,上午1:48'
# ____________________分割线___________________
from django.test import TestCase

# Create your tests here.
# 循环生成u'A'-u'Z'的元组
Alphabetical = ()
for ch in xrange(0x41, 0x5B):
    Alphabetical =Alphabetical+((unichr(ch),unichr(ch)),)
print Alphabetical


