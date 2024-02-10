from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views.generic import ListView, DetailView
# from django.template import loader
# Create your views here.

class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Returns the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]


class QuestionDetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"



# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # output = ", ".join([q.question_text for q in latest_question_list])
#     template = "polls/index.html"
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     return render(request, template, context)

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     template = "polls/index.html"
#     context = {
#         "question": question
#     }
#     return render(request, template, context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     template = "polls/results.html"
#     context = {
#         "question": question
#     }
#     return render(request, template, context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        template = "polls/detail.html"
        context = {
            "question": question,
            "error_message": "You didn't select a choice"        
            }
        return render(request, template, context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
