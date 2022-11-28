from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.
# def demo(request):
#     # return HttpResponse("Hello World")
#     return render(request,"sum.html")
#
# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("This is contact info")

def pass_value(request):
    # name='India'
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
