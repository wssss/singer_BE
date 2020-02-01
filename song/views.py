from rest_framework.generics import ListCreateAPIView
from .models import SongGroup, Song
from .serializers import SongGroupSerializer,SongSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

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