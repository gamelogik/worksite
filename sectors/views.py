from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ApplyForm
from .models import Cvs

from itertools import chain

# Create your views here.

from . import models, forms

from .models import Sector, Job, Question


def sector_list(request):
    sectors = Sector.objects.all()
    return render(request, 'sectors/sector_list.html', {'sectors': sectors})

def sector_detail(request, pk):
    sector = get_object_or_404(models.Sector, pk=pk)
    jobs = sorted(chain(sector.text_set.all(), sector.quiz_set.all()),
                  key=lambda job: job.order)
    return render(request, 'sectors/sector_detail.html', {
        'sector': sector,
        'jobs': jobs
    })


def text_detail(request, sector_pk, job_pk):
    job = get_object_or_404(models.Text, sector_id=sector_pk, pk=job_pk)
    return render(request, 'sectors/job_detail.html', {'job': job})


def quiz_detail(request, sector_pk, job_pk):
    job = get_object_or_404(models.Quiz, sector_id=sector_pk, pk=job_pk)
    return render(request, 'sectors/job_detail.html', {'job': job})


def apply_view(request, sector_pk, job_pk):
    form = forms.ApplyForm()
    job = get_object_or_404(models.Text, sector_id=sector_pk, pk=job_pk)
    if request.method == 'POST':
        form = forms.ApplyForm(request.POST)
        if form.is_valid():
            send_mail(
                'Application from {}'.format(form.cleaned_data['name']),
                form.cleaned_data['motivation'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['Jamsie@teamie.com']
            )
            messages.add_message(request, messages.SUCCESS,
                                 'Thanks for your application!')


            cvs = form.save()
            return HttpResponseRedirect(reverse('sectors:apply', kwargs={'sector_pk': sector_pk, 'job_pk': job_pk}))

    return render(request, 'sectors/apply_form.html', {'job': job, 'form': form})


    ## as you can see above, the views of job_detail and apply are the same but
    ## they need to named different as the html reference is different.

    ## also, since we didn't have to create new arguments for this page
    ## the Job class is enough...
