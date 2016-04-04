# -*- coding: utf-8 -*-
# __author__ = 'neo'
# __name__ = '王腾蛟'
# __time__ = '2015年,上午1:48'
# ____________________分割线___________________
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Album, Music


@require_http_methods(["GET", "POST"])
def album(request, album_id):
    # 专辑列表
    album_list = Album.objects.get(ID=album_id)
    music_list = Music.objects.filter(Album_id=album_id)
    cont = {'album': album_list, 'music': music_list, }
    return render(request, 'web/albumID.html', cont)
