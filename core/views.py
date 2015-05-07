from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SplashView(TemplateView):
	"""docstring for ClassName"""
	template_name = "index.html"
	