from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def index(request):

    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def properties(request):

    return render(request, 'properties.html')


def property_details(request):
    return render(request, 'property_details.html')



