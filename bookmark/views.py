from django.shortcuts import render
from django.views import ListView, DetailView

from bookmark.models import Bookmark

# Create your views here.
class BOokmarkLIstView(ListView):
    model = Bookmark


#장고에서는 자동적으로 지정해주는 속성 2가지가 있다.
#컨텍스트 변수 : object_list로 지정    
#템플릿 파일 : 모델명소문자_list.html로 지정 ------------> bookmark_list.html

class BookmarkDetailView(DetailView):
    model = Bookmark
#컨텍스트 변수 : object
#템플릿 파일명 : 모델명소문자_detail.html ------------> bookmark_detail.html