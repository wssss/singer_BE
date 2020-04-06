from rest_framework import serializers
from .models import SongGroup, Song, SongList
from django.shortcuts import get_object_or_404 
from users.models import User


class SongGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongGroup
        fields = ["id", "name", "user_id" ]
        extra_kwargs ={
            "id":{
                "read_only":True
            }
        }

    def validate(self, data):
        name = data.get("name")
        if len(name) < 2 or len(name) > 20:
            raise serializers.ValidationError("名称过长！")

        return data

    def create(self, validate_data):
        name=validate_data.get("name")
        user = self.context['request'].user
        
        group = SongGroup.objects.create(
            name=name,
            user = user
        )
        return group
    
        


class SongSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(required=False, label="分组id", write_only=True,allow_null=True)
    class Meta:
        model = Song
        fields = ["id", "name", "singer", "group_id", "group"]
        depth = 1
        extra_kwargs = {
            "singer":{
                "allow_null":True
            },
            "group":{
                "read_only":True
            }
        }
    
    def validate(self, data):
        name=data.get("name")
        singer=data.get("data")
        if len(name) < 1 or len(name)>30:
            raise serializers.ValidationError("名称过长或过短")

        return data

    def create(self, validate_data):
        name=validate_data.get("name")
        singer=validate_data.get("singer")
        user=self.context['request'].user
        group_id = validate_data.get("group_id")
        try:
            group=SongGroup.objects.get(pk=group_id)
        except SongGroup.DoesNotExist:
            group=None
        song = Song.objects.create(
            name=name,
            singer=singer,
            user=user,
            group=group
        )
        return song


class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["name", "group_id", "singer"]


class OrderSongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields = ["id", "name", "singer",  "group"]
        depth=1



class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model=SongList
        fields=[ "song", "create_time", "sang_time", "sponsor", "money", "is_sang"]

    def create(self, validated_data):
        try:
            
            user=User.objects.get(pk=self.context['view'].kwargs.get('pk'))
        except User.DoesNotExist:
            raise serializers.ValidationError("请输入歌手id")

        song = SongList.objects.create(
                user=user,
                song=validated_data.get("song"),
                sponsor=validated_data.get("sponsor"),
                money=validated_data.get("money")
            )
        return song