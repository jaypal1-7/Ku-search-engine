#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 07:06:17 2022

@author: jaypalsingh
"""

from django.shortcuts import render
from vector_model import *

#eender the first page for query 
def Home(request):
     return render(request, 'personal/index1.html')

#schedule the search details page
def search_query(request, tosearch):

    query = request.GET.get('tosearch',None)    
    try:
        newq = main_func(query)
        return render(request, 'personal/index2.html', {'newq':newq})
    except (TypeError,ValueError):
        pass

#Schedule our relevance feedback page
def relevance_feedback(request, reldoc, reldoc1):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['editbox1']
    else:
        docname = request.GET.get('reldoc')    
        new_reldoc = relevance_feedback(docname)

    return render(request, 'personal/index3.html', {'new_reldoc':new_reldoc})