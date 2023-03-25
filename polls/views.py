from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    #ListView에서 자동 생성되는 컨텍스트 변수는 object_list 여기서 말하는 object는
    #question이다 자동 생성되는 컨텍스느 변수는 question_list
    #context_object_name 속성을 이용하여 오버라이딩 해준다.
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')
class DetailView(generic.DetailView):
    model = Question
    template_name ='polls/detail.html'

    #DetailView에서도 모델이 Question이기 때문에 Django에서는 context 변수의 이름을 question으로 결정

class ResultsView(generic.DetailView):
    model =Question
    template_name='polls/results.html'

def vote(request, question_id):
    question =get_object_or_404(Question, pk=question_id)
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

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))# args는 튜플 형탠
