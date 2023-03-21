from django.urls import path
from . import views
# 하나의 project에 여러개의 app을 사용한다면(일반적으로 여러개의 app을 사용함)
# URLconf에 네임스페이스(namespace)를 추가해야 한다. 왜냐하면 Django가{% url %}태그를 사용하여 어떤 app의
# view에서 URL을 생성해야 하는 지를 알 수 있기 때문이다.
app_name =  'polls'

urlpatterns =[
    path('',views.index),
    path('<int:question_id>/', views.detail, name='detail'), #polls/10 or /10  =>question_id=10
    path('<int:question_id>/results', views.results,name='results'),
    path('<int:question_id>/vote', views.vote,name='vote'),
]