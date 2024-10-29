from django.shortcuts import render

# Create your views here.
def funcpres(request):
    return render(request, 'func.html')

def classpres(request):
    return render(request, 'clas.html')