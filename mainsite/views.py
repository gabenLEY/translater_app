from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator

def home(request):
    if request.method == 'POST':
        text = request.POST['lang1']
        translator = Translator()
        lang = translator.detect(text).lang
        transalation = translator.translate(text).text
        destination = translator.translate(text).dest
        print(destination)
        context = { 
                   "text" : transalation, 
                   "send" : text, 
                   "ori" : lang,
                   "dest" : destination,
                   }
        return render(request,"index.html", context)
    return render(request, "index.html")
