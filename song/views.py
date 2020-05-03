from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView, ListAPIView,CreateAPIView
from rest_framework.views import  APIView
from .models import SongGroup, Song,SongList
from .serializers import SongGroupSerializer,SongSerializer, SongDetailSerializer, OrderSongSerializer,SongListSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response

class GroupAPIView(ListCreateAPIView):
    serializer_class = SongGroupSerializer
    authentication_classes  = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return SongGroup.objects.filter(user_id=self.request.user)
    



class SongAPIView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return Song.objects.filter(user_id=self.request.user)



class SongDetailView(APIView):

    def put(self, request, pk):
        song = Song.objects.filter(pk=pk).first()
        ser_obj = SongDetailSerializer(song, data=request.data)
        if ser_obj.is_valid():
            ser_obj.uesr_id = request.user
            ser_obj.save()
            return Response(ser_obj.data)
        else:
            return Response(ser_obj.errors)

    def delete(self, request, pk):
        song = Song.objects.filter(pk=pk).first()
        if song:
            song.delete()
            return Response("删除成功！")
        else:
            return Response("删除对象不存在！")
    

class groupDeleteView(APIView):
    def delete(self, request, pk):
        group = SongGroup.objects.filter(pk=pk).first()
        if group:
            group.delete()
            return Response("删除成功")
        else:
            return Response("删除对线不存在")




class OrderListView(ListAPIView):
    serializer_class =  OrderSongSerializer 
    
    def get_queryset(self):
        return Song.objects.filter(user_id=self.kwargs['pk'])


class SongToSingCreateView(ListCreateAPIView):
    serializer_class = SongListSerializer
    permission_classes=(AllowAny,)

    def get_queryset(self):
        return SongList.objects.filter(user_id=self.kwargs.get('pk'))



    
