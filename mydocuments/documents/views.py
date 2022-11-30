from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def personal_document(request, name):
    doc = None
    if name == "RG":
        doc = "13.686.152-0"
    elif name == "CPF":
        doc = "799.884.289-01"
    elif name == "CEP":
        doc = "70767-090"
    else:
        return HttpResponseNotFound("This document is not supported!")
    return HttpResponse(doc)

