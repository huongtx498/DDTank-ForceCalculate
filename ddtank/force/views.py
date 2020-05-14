import math
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HomeForm
from .models import Ddtank
from .serializers import DdtankSerializer
from rest_framework import generics


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Ddtank.objects.all()
    serializer_class = DdtankSerializer


def home(request):
    g = float()
    l = float()
    homeForm = HomeForm()
    if request.method == 'POST':
        homeForm = HomeForm(request.POST or None)
        response = HttpResponse()
        d = math.floor(float(request.POST['khoangcach']))
        h = math.floor(float(request.POST['docao']))
        v = float(request.POST['gio'])
        a = request.POST['cachban']
        g = math.floor(90 - d + 2*v + h/4)
        l = 95 + (float(request.POST['khoangcach'])-d)*4
    context = {
        'goc': g,
        'luc': l
    }

    return render(request, 'force/home.html', {'context': context, 'form': homeForm})
