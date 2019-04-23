from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializers
from .models import Music


# Create your views here.
# Response 를 통해 Serializer 를 반환
# Serializer -  특정한 딕셔너리 혹은 쿼리셋 등 파이썬 형식 데이터 타입을 반환하도록 해주는 아이.

# music 는 쿼리셋, 일종의 리스트인데 우리가 응답하려고 하는 것은 json
# Serializer 가 해주는 것은 리스트를 하나하나씩 json타입으로 바꿔주는 고마운 도구
# 그리고 응답하는 함수는 Respone 이다.
#결과로 보내줄 데이터는 .data 로 가져온다.

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    seializer = MusicSerializers(musics, many = True)
    return Response(serializer.data)