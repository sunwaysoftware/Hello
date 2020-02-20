from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models.finance import Contracts


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Contracts.objects.order_by('-award_date')[:5]


class DetailView(generic.DetailView):
    #model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'


def vote(request, question_id):
    template_name = 'polls/results.html'