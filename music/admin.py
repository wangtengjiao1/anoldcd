# -*- coding: utf-8 -*-
# __author__ = 'neo'
# __name__ = '王腾蛟'
# __time__ = '上午1:48'
# ____________________分割线___________________
from django.contrib import admin
from .models import *

ModelsName = [Press, Musician, Album, Music]
name = ('Name', 'Status', 'CreatedTime', 'ChangeTime',)


# 基本信息内容,将其展示到admin当中
class BasicAdmin(admin.ModelAdmin):
    # 显示表头
    list_display = name
    # 显示右侧过滤器
    list_filter = name
    # 搜索功能
    search_fields = name
    # 排序 当前按照修改时间排序
    ordering = name


class FlatPageAdmin(admin.ModelAdmin):
    fields = ()

# 注册到admin当中
for name in ModelsName:
    admin.site.register(name, BasicAdmin)

