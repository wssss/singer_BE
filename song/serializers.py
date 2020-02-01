from rest_framework import serializers
from .models import SongGroup, Song
from django.shortcuts import get_object_or_404 

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
    group_id = serializers.IntegerField(required=False,label="组id",write_only=True)
    # group = SongGroupSerializer()
    class Meta:
        model = Song
        fields = ["name", "singer", "group_id", "group"]
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
        print(group)
        song = Song.objects.create(
            name=name,
            singer=singer,
            user=user,
            group=group
        )
        return song
