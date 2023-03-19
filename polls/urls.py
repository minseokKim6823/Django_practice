from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('<int:question_id>', views.detail, name='detail'), #polls/10 or /10  =>question_id=10
    path('<int:question_id>/result', views.result),
    path('<int:question_id>/vote', views.vote),
    
]