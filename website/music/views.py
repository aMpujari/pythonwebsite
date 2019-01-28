from django.http import HttpResponse
from django.template.context_processors import request
from django.shortcuts import render, HttpResponse, redirect 

def index(request):
    return HttpResponse('<h1> This is music app home page')
def about(request):
    return HttpResponse('<h1> This is music about home page')
def welcome(request):
    return render(request, 'account/welcome.html')
def create(request):
    print(request.method)
    if request.method == "POST":
        print('*'*50)
        print(request.POST)
        print('*'*50)
    else:
        return redirect('../music/welcome') 
def msg(request):
    return render(request, 'account/message.html')
    
    