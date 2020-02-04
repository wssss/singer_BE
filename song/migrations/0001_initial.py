# Generated by Django 2.2 on 2020-01-29 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='歌曲名称')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('singer', models.CharField(max_length=50, verbose_name='原唱歌手')),
                ('is_pub', models.BooleanField(default=True, verbose_name='是否发布')),
            ],
            options={
                'verbose_name': '歌曲',
                'verbose_name_plural': '歌曲',
                'db_table': 'singer_song',
            },
        ),
        migrations.CreateModel(
            name='SongList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='点歌时间')),
                ('sang_time', models.DateTimeField(auto_now=True, verbose_name='唱歌时间')),
                ('sponsor', models.CharField(max_length=50, verbose_name='打赏人')),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='打赏金额')),
                ('is_sang', models.BooleanField(default=False, verbose_name='是否已唱')),
                ('song', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='song.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '点歌列表',
                'verbose_name_plural': '点歌列表',
                'db_table': 'singer_song_list',
            },
        ),
        migrations.CreateModel(
            name='SongGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='分组名称')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '歌曲分组',
                'verbose_name_plural': '歌曲分组',
                'db_table': 'singer_song_group',
            },
        ),
        migrations.AddField(
            model_name='song',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='song.SongGroup', verbose_name='分组名称'),
        ),
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]