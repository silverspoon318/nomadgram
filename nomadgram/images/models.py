from django.db import models

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #이 모델은 데이터베이스를 생성하기 위해 사용되지 않는다., 다른 모델들을 위한 base로 사용된다.

class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length = 140)
    caption = models.TextField()

class Comment(TimeStampedModel):
    
    message = models.TextField()
