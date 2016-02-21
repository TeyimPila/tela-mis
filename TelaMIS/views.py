
## [Created by SkaeX @ 2016-02-21 15:58:46] 

# -*- coding: utf-8 -*-
from django.shortcuts import render
def home(request):
	return render(request, "TelaMIS/index.html", {})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")