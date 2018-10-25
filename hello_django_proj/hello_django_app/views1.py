from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "Hey You, Yes You!",
                "message": "Welcome to my World"}
        return data
    
class AboutPageView (TemplateView):
    template_name = "about.html"
    def get_context_data(self):
        data = {"message_title" : "Attention",
                "message": "UBUNTU UBUNTU"}
        return data
    

