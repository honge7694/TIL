from django.db import models


class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add : 최초 생성 시간을 1번 사용하여 저장, 갱신 불가능
    updated_at = models.DateTimeField(auto_now=True) # auto_now : 장고 모델이 저장될때마다 현재날짜(시간)으로 갱신, 갱신 가능

    def __str__(self):
        # return f"Custom Post object ({self.message})"
        return self.message
        
    # 모델에 정의되어 있지 않아도 함수로 list_display 가능.
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자 수"




