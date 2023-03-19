from django.shortcuts import render
from django.http import HttpResponse 
#웹서버에서 실행되는 코드 응답을 위해서 Response 객체 필요 요청시는 Request객체 서버 응답은 Response

from .models import Question #models.py에Question 함수 있음
# Create your views here.
def index(request):
    #questions =Question.objects.all()
        #str=''
        #for question in questions:
        #   str += "{} 날짜 : {} <br/>".format(question.question_txt,question.pub_date)
        #   str += "--------------<br/>"
        #return HttpResponse(str)
    #context = {'questions': questions}
    #return render(request, 'temp_test/index.html', context)
    latest_question_list =Question.objects.order_by('-pub_date')
    output = ', '.join([q.question_txt for q in latest_question_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse("당신은 %s번 질문을 보고 있습니다." %question_id)

def result(request, question_id):
    return HttpResponse("당신은 %s번 질문의 결과를 보고 있습니다." %question_id)

def vote(request, question_id):
    return HttpResponse("당신은 %s번 질문에 투표를 합니다." %question_id)