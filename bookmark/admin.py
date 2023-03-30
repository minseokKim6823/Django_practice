from django.contrib import admin

from bookmark.models import Bookmark

# Register your models here.
# Bookmark 클래스가 Admin사이트에서 어떻게 보일지를 정의하는 클래스
class BookmarkAdmin(admin.ModelAdmin):
    list_display =('title','url') #Bookmark의 내용을 보여 줄때 title과 url을 화면에 보이도록


admin.site.register(Bookmark,BookmarkAdmin)
