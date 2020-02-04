from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

class SongGroup(models.Model):
    name = models.CharField(verbose_name="分组名称", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table="singer_song_group"
        verbose_name_plural = verbose_name = "歌曲分组"

    def __str__(self):
        return self.name


#点歌歌曲
class Song(models.Model):
    name = models.CharField(verbose_name="歌曲名称", max_length=50)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    singer = models.CharField(_("原唱歌手"), max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(SongGroup, verbose_name=_("分组名称"), on_delete=models.CASCADE, blank=True, null=True, related_name="songs")
    is_pub = models.BooleanField(verbose_name="是否发布", default=True)

    class Meta:
        db_table="singer_song"
        verbose_name_plural = verbose_name = "歌曲"

    def __str__(self):
        return self.name
    
#点歌列表
class SongList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="点歌时间", auto_now=True)
    sang_time = models.DateTimeField(verbose_name="唱歌时间", auto_now=True)
    sponsor = models.CharField(verbose_name="打赏人",max_length=50)
    money = models.DecimalField(verbose_name="打赏金额",max_digits=6,decimal_places=2,default=0)
    is_sang = models.BooleanField(verbose_name="是否已唱", default=False)


    class Meta:
        db_table="singer_song_list"
        verbose_name_plural = verbose_name = "点歌列表"