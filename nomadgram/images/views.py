from rest_framework.views import APIView
from rest_framework.response import Response    # 엘리먼트를 가져오고 보여주고 method를 관리하는 클래스
from . import models, serializers

class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)

class ListAllComments(APIView):

    def get(self, request, format = None):
        
        all_comments = models.Comment.objects.all()

        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(serializer.data)

class ListAllLikes(APIView):

    def get(self, request, format = None):
    
        all_likes = models.Like.objects.all()

        serializer = serializers.LikeSerializer(all_likes, many = True)

        return Response(serializer.data)