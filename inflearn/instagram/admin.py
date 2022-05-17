from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment


# 방법 1
# admin.site.register(Post)

# 방법 2
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)

# 방법 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at'] # list_display : 모델 리스트에 출력할 컬럼을 지정할 수 있다.
    list_display_links = ['message'] # list_display_links : 링크가 될 칼럼을 지정할 수 있다.
    list_filter = ['created_at', 'is_public'] # list_filter : 지정 필드값으로 필터링 옵션이 제공된다.
    search_fields = ['message'] # search_fields : admin 내 검색 UI를 통해, DB를 통한 where 쿼리 대상 필드 리스트를 출력한다.
    

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None

    # 모델에 정의되어 있지 않아도 함수로 list_display 가능.
    def message_length(self, post):
        return f'{len(post.message)} 글자'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass