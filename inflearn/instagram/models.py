from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add : 최초 생성 시간을 1번 사용하여 저장, 갱신 불가능
    updated_at = models.DateTimeField(auto_now=True) # auto_now : 장고 모델이 저장될때마다 현재날짜(시간)으로 갱신, 갱신 가능

    def __str__(self):
        # return f"Custom Post object ({self.message})"
        return self.message

    def get_absolute_url(self):
        return reverse("instagram:post_detail", args=[self.pk])
    
    

    class Meta:
        ordering = ['-id']
        # python manage.py shell_plus --print-sql을 이용하여 좀 더 편하게 볼 수 있다.
        # 실행 시킨 후, from instagram.models import Post import 해줘야 한다.

    # 모델에 정의되어 있지 않아도 함수로 list_display 가능.
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자 수"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, limit_choices_to={'is_public': True})
    # post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE) 문자열을 이용하여 다른 앱을 import 하지 않고 사용 가능하다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)
    
    def __str__(self):
        return self.name

