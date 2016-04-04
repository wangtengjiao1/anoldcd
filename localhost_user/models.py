# -*- coding: utf-8 -*-
# __author__ = 'neo'
# __name__ = '王腾蛟'
# __time__ = '2015年,上午1:48'
# ____________________分割线___________________
from __future__ import unicode_literals
from basic.models import *
from django.contrib.auth.models import User


# 管理员部分
class Administrator(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(u'管理员姓名', max_length=50)
    Administrator = models.OneToOneField(User, verbose_name=u'基本用户')
    Signature = models.CharField(u'签名', max_length=100, default='这家伙很懒,什么都还没有维护!')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'管理员'
        verbose_name_plural = u'管理员管理'

    def __unicode__(self):
        return self.Name

