from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.template import loader
from django.http import HttpResponse
from . import hackathon
import os
import json


# Create your views here.
class Home(TemplateView):
    template_name='home.html'

def render_upload(request):
    template = loader.get_template('home.html')
    context = {
    }
    if request.method == 'POST':
        uploaded_file=request.FILES.getlist('document')
    
        fs=FileSystemStorage()
        for item in uploaded_file:
            fs.save("./media/"+item.name,item)
        
        try:
            os.remove("resultat.json")
        except:
            print("il n'y pas de json") 

        hackathon.demarrer()
        with open('resultat.json', 'r') as f:
         my_json_obj = json.load(f)
         context = {
            'images': my_json_obj["tab"]
         }
         f.close()
        

    return HttpResponse(template.render(context, request))

