# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
def home(request):
	text = """<h1>Bienvenue sur mon blog !</h1>
	<p>L'assebleur ça tue ce qui ne connait pas!</p>"""
	return HttpResponse(text)