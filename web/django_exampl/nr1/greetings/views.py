from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def hello_world(request):
    return HttpResponse("Hello world")

def hello_name(requests,name):
    return HttpResponse(f"Hello {name}")
# Create your views here.