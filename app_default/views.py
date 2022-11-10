import json

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Question, Choice
from rest_framework import  generics
from .serializers import QuestionSerializer
from rest_framework.views import APIView

# Create your views here.


class ReservationListView(APIView):
     def post(self, request):
          data = json.loads(request.body)
          
          serializer = QuestionSerializer(data=data)
          if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data, status=201)
          else:
               return  JsonResponse(serializer.errors, status=404)
          
     def get(self, request):
          reservation = Question.objrcts.all()
          serializer = QuestionSerializer(reservation, many=True)
          
          return JsonResponse({'data':serializer.data}, status=200)
     
def index(request):
     
     latest_question_list = Question.objects.order_by('-pub_date')[:5]
     
     context = {
          'latest_question_list': latest_question_list,
     }
     
  
     return render(request, 'app_default/index.html', context)

def detail(request, question_id):
  
     question = get_object_or_404(Question, pk=question_id)
     
     try:
          selected_choice = question.choice_set.get(pk=request.POST['choice'])
     except (KeyError, Choice.DoesNotExist):
          return render(request, 'app_default/detail.html', {
               'question': question,
               'error_message':"You didn't select a choice.",
          })
     else:
          selected_choice.votes += 1
          selected_choice.save()
     
     return HttpResponseRedirect(reversed('app_defaul:results', args=(question.id)))

def results(request, question_id):
     response = "You're looking at the result of question %s."
     return HttpResponse(response %question_id)
def vote(request, question_id):
     question = get_object_or_404(Question, pk=question_id)
     
