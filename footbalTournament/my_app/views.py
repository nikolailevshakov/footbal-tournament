from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def simple_view(request):
    my_var = {'first_name': 'Nik', 'last_name': 'Lev',
              'some_list': [1, 2, 3],
              }
    return render(request, 'my_app/example.html', context=my_var)


