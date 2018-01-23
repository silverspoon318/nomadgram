from rest_framework import serializers
from . import models

class ImageSerializer(serializers.ModelSerializer):
    # Meta 설정하는 클래스
    class Meta:
        model = models.Image
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    image = ImageSerializer()

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    # nested serialize, foreign key 가 아니라 이미지 시리얼라이저, 이미 시리얼라이즈가 구축되어 있기 때문에 키가 아닌 시리얼라이즈로 노출된다.
    image = ImageSerializer()

    class Meta:
        model = models.Like
        fields = '__all__'