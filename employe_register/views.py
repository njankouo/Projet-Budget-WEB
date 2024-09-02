from django.shortcuts import render
from tutorial.models import Institution
# Create your views here.

def employee_list(request):
    institutions=Institution.objects.all()
    context={
        'institutions':institutions
    }
    template='../website/employe.html'
    return render(request,template,context)

# def employee_delete(request):


# def employee_update(request):


# def employee_save(request):


def position(request):
    template='../website/position.html'
    return render(request,template)
