from django.shortcuts import render
from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def add(request,first,second):
    return HttpResponse(f"{first}+{second}={int(first)+int(second)}")

def sub(request,first,second):
    return HttpResponse(f"{first}-{second}={int(first)-int(second)}")
def multiply(request,first,second):
    return HttpResponse(f"{first}*{second}={int(first)*int(second)}")
def divide(request,first,second):
    return HttpResponse(f"{first}/{second}={float( first)/float(second)}")
def smth(request,first,second):
    return HttpResponse(f"{first}/{second}={float( first)/float(second)}")
# Create your views here.
