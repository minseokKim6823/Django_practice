from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse ,HttpResponseNotFound, HttpResponseRedirect
#웹서버에서 실행되는 코드 응답을 위해서 Response 객체 필요 요청시는 Request객체 서버 응답은 Response
from django.template import loader
from django.http import Http404

from .models import Question #models.py에Question 함수 있음
# Create your views here.
def index(request):
    # questions =Question.objects.all()
        #str=''
        #for question in questions:
        #   str += "{} 날짜 : {} <br/>".format(question.question_txt,question.pub_date)
        #   str += "--------------<br/>"
        #return HttpResponse(str)
    # context = {'questions': questions}
    # return render(request, 'temp_test/index.html', context)

    # latest_question_list =Question.objects.order_by('-pub_date')
    # output = ', '.join([q.question_txt for q in latest_question_list])
    # return HttpResponse(output)

    #아니면

    # latest_question_list = Question.objects.order_by('-pub_date')
    # template = loader.get_template('polls/index.html')
    # context = {'latest_question_list':latest_question_list}
    # return HttpResponse(template.render(context, request))

    #아니면

    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}

    # render함수는 request객수를 첫번째 인수로받고,template이름을 두번째 인자로 사용, 
        # 세번째 인자는 (optional)인자로 컨텍스트(사전형 객체)를 받는다.
        # render함수는 HttpResponse객체를 리턴한다
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    #-------------------------------------------------------------
    # try:
    #     question = Question.objects.get(pk=question_id)
    # #except Question.DoesNotExist:
    #    # raise Http404("질문이 존재하지 않습니다.") 404문 뜨게 하기
    # except:
    #     return HttpResponseNotFound("없는 질문 입니다.")
    #-------------------------------------------------------------
    question =get_object_or_404(Question,pk = question_id)#id값을 받고 53번째줄 이동

    #return HttpResponse("당신은 %s번 질문을 보고 있습니다." %question_id)
    return render(request, 'polls/detail.html', {'question': question})#50번째줄 question 객체가 넘어가서 detail뷰에서 호출

def result(request, question_id):
    return HttpResponse("당신은 %s번 질문의 결과를 보고 있습니다." %question_id)

def vote(request, question_id):
    question =get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message':"선택 에러 입니다.",
            })
    else:
        selected_choice.votes+=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=question.id,))
        # POST 데이터 처리가 성공적으로 이루어 지면 항상 HttpResponseRedirect를 리턴한다. 
        # 이 방법을 통해 유저가 브라우저의 뒤로가기 버튼을 눌렀을 때 데이터가 두 번 저장되는 것을 방지 할 수 있다.
        # 이 방법은 모든 웹개발에 적용된다.

        #reverse()함수는 뷰의 이름과 뷰를 가리키는 URL패턴의 일부인 변수를 전달 받아서
        #문자열로 리턴한다. 예> '/polls/4/results/'

    #return HttpResponse("당신은 %s번 질문에 투표를 합니다." %question_id)

#request.POST : 사전과 같은 객체이다
#request.POST['choice'] : 선택된 설문의 ID를 문자열로 반환 (request.POST는 항상 문자열로 반환)