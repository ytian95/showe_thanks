from django.shortcuts import render

# Create your views here.
def gantt(request):
    return render(request, 'main/gantt.html')