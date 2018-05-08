# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone 

from django.http import HttpResponse
from django.shortcuts import render 
from .models import Cubedata

# Test index 

def table(request):  
	tables = Cubedata.objects.all() 
	template_name = "data/table.html" 
	data = { 
		'tables' : tables , 
	} 
	return render_to_response (template, data, 
		context_instance = RequestContext( request ))

	

