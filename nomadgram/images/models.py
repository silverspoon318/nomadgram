from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram.users import models as user_models

@python_2_unicode_compatible
class TimeStampedModel(models.Model):
    
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #이 모델은 데이터베이스를 생성하기 위해 사용되지 않는다., 다른 모델들을 위한 base로 사용된다.

@python_2_unicode_compatible
class Image(TimeStampedModel):

    """ Image Model """
    id = 1
    file = models.ImageField()
    location = models.CharField(max_length = 140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True) # image 를 생성한 사람

    # meta class, string representation : string 이 어떻게 보이느냐
    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

@python_2_unicode_compatible
class Comment(TimeStampedModel):
    
    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True)
    image = models.ForeignKey(Image, null=True, related_name='comments')  # 연결된 이름이란, 이미지는 댓글을 찾을거고, 댓글을 찾는 방법은 그들의 '연결된 이름'을 부르는 방법
    # 결국 set은 서로 연결된 모델을 그룹핑 하는 방법

    def __str__(self):
        return self.message

@python_2_unicode_compatible
class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, null=True)
    image = models.ForeignKey(Image, null=True, related_name='likes')

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)