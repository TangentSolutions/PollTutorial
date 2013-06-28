from django.http import HttpResponse
from polls.models import Poll
from django.shortcuts import render, get_object_or_404

def index(request):

    polls = Poll.objects.all()

    context = {
        'polls': polls,
    }
    return render(request, 'polls.html', context)    

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {'poll': poll}
    return render(request, 'poll.html', context)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)