from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll
from django.views import generic


class IndexView(generic.ListView):
    
    template_name = 'polls.html'
    context_object_name = 'polls'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.all()


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'poll.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)

    
    try:
        
        selected_choice = p.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect("/polls/%s/results/" % poll_id)