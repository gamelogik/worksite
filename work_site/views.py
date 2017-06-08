from django.shortcuts import render
from sectors.models import Job

def hello_world(request):
    return render(request, 'home.html')

from django.http import HttpResponse
from django.template import loader, Context



from django.views import generic
from django.shortcuts import render
from sectors.models import Job

class IndexView(generic.ListView):
    template_name = 'search_results.html'
    page_template = 'base.html'
    context_object_name = 'all_movies'
    model = Job

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'all_genres': Job.objects.all(),
            'page_title': 'Latest'
        })
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Job.objects.filter(title__icontains=query)
        else:
            return Job.objects.all()