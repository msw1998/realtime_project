from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'newapp/index.html',context={'text':'Hello World','text2':'32'})
