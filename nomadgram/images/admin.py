from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    # pass    # 텅 빈 클래스를 의미한다.

    list_display_links = (
        'location',
    )

    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
        'creator',
    )

    list_display = (
        'file',
        'location',
        'caption',
        'creator',
        'created_dt',
        'updated_dt',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display =  (
        'creator',
        'image',
        'created_dt',
        'updated_dt',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'message',
        'creator',
        'image',
        'created_dt',
        'updated_dt',
    )