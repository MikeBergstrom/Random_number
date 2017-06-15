# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string

from django.shortcuts import render

def index(request):
    print "in index"
    request.session['counter'] = 0
    return render(request, 'randoo/index.html')

def generate(request):
    print "generate"
    request.session['counter'] = request.session['counter'] +1
    request.session['randomWord'] = ""
    for i in range(1,14):
        request.session['randomWord'] += (random.choice(string.letters))
    print request.session['randomWord']
    return render(request, 'randoo/index.html')


# Create your views here.
