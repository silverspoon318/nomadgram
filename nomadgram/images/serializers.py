from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer):
    # Meta 설정하는 클래스
    class Meta:
        model = models.Image
        fields = '__all__'

class CommentSerializer(serializers.Serializer):
    
    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.Serializer):

    class Meta:
        model = models.Like
        fields = '__all__'