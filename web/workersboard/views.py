from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.

from .models import Workers as ws

def main_page(request):
    return HttpResponse('<h4 align="center">main page</h4')

# def board(request):
#    template = loader.get_template('wb/workers_board.html')
#    wsb = ws.objects.order_by('-date')
#    context = { 'wsb' : wsb  }
#    return HttpResponse(template.render(context, request))

def board(request):
    wsb = ws.objects.order_by('-date')
    return render(request, 'wb/workers_board.html', { 'wsb' : wsb })