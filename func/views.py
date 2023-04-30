from django.shortcuts import render
from django.http import HttpResponse
from .funcs.function import scrapeData

def index(request):
    if request.method == "GET":
       
        return render(request, "index.html")
    else:
        
        input1 = request.POST.get("input1")
        input2 = request.POST.get("input2")
        input3 = request.POST.get("input3")
        data = scrapeData(input1, input2, input3)

        return render(request, "index.html", {"data": data})
        