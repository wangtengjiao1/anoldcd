# -*- coding: utf-8 -*-
# __author__ = 'neo'
# __name__ = '王腾蛟'
# __time__ = '2015年,上午1:48'
# ____________________分割线___________________
from __future__ import unicode_literals
from basic.models import *
from localhost_user.models import *
# 导入uuid功能
import uuid
# 时间戳
import time

now = time.strftime("%Y/%m/%d/")


# 出版社模型
class Press(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(u'出版社名称', max_length=50)
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'出版社'
        verbose_name_plural = u'出版社管理'

    def __unicode__(self):
        return self.Name


# 音乐家姓名
class Musician(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(u'音乐家姓名', max_length=50)
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'音乐人'
        verbose_name_plural = u'音乐人管理'

    def __unicode__(self):
        return self.Name


# 专辑信息
class Album(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(u'专辑名称', max_length=50)
    LongName = models.CharField(u'长名称', max_length=50, null=True, blank=True)
    Score = models.IntegerField(u'评分', null=True, blank=True, default=3)
    AlphabeticalIndex = models.CharField(u'字母索引', max_length=10)
    Press = models.ForeignKey(Press, verbose_name=u'出版社', null=True, blank=True)
    ReleaseTime = models.DateTimeField(u'发布时间', )
    Musician = models.ManyToManyField(Musician, verbose_name=u'音乐人')
    Class = models.ForeignKey(Class, verbose_name=u'分类')
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    Label = models.ManyToManyField(Label, verbose_name=u'标签')
    ImgUrl = models.ImageField(u'专辑图片', upload_to='pic_folder/' + now, default='pic_folder/None/no-img.jpg', null=True,
                               blank=True)
    Details = models.TextField(u'专辑详情', null=True, blank=True)
    AccessAmount = models.IntegerField(u'访问量', null=True, blank=True, default=0)
    Administrator = models.ForeignKey(Administrator, verbose_name=u'维护人')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'专辑'
        verbose_name_plural = u'专辑管理'

    def __unicode__(self):
        return self.Name


# 音乐信息
class Music(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(u'音乐名称', max_length=50)
    LongName = models.CharField(u'长名称', max_length=50, null=True, blank=True)
    Score = models.IntegerField(u'评分', null=True, blank=True, default=3)
    Album = models.ForeignKey(Album, verbose_name=u'专辑名称')
    AlphabeticalIndex = models.CharField(u'字母索引', max_length=10)
    Press = models.ForeignKey(Press, verbose_name=u'出版社')
    ReleaseTime = models.DateTimeField(u'发布时间', )
    Musician = models.ManyToManyField(Musician, verbose_name=u'音乐人')
    Class = models.ForeignKey(Class, verbose_name=u'分类')
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    Label = models.ManyToManyField(Label, verbose_name=u'标签')
    ImgUrl = models.ImageField(u'音乐图片', upload_to='pic_folder/' + now, default='pic_folder/None/no-img.jpg', null=True,
                               blank=True)
    Details = models.TextField(u'音乐详情', null=True, blank=True)
    Order = models.IntegerField(u'专辑内顺序', null=True, blank=True, default=0)
    AccessAmount = models.IntegerField(u'访问量', null=True, blank=True, default=100)
    DataUrl = models.FileField(u'文件地址', upload_to='music/' + now, null=True, blank=True)
    Administrator = models.ForeignKey(Administrator, verbose_name=u'维护人')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'音乐'
        verbose_name_plural = u'音乐管理'

    def __unicode__(self):
        return self.Name