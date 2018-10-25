from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "Favorite Quote",
                "message": "Best Definition of birthday: The only day in your life, your mother smiled when you cried"}
        return data
    
class AboutPageView (TemplateView):
    template_name = "resume.html"
    def get_context_data(self):
        data = {"message_title" : "Education",
                "message1": "Senior High School: Camarines Sur National High school",
                "message": "Elementary: Rosario V. Maramba Elementary School"}
        return data

class ContactInfoPageView (TemplateView):
    template_name = "contactInfo.html"
    def get_context_data(self):
        data = {"message_title" : "Cyrus Kim A. Requiro",
                "message1": "Address: Zone 7, San Felipe Naga City",
                "message2": "Email: cyrus.inflame@gmail.com",               
                "message3": "Mobile No. 09464010757"}
        return data

