from django.shortcuts import render,HttpResponse

# Create your views here.
def about_view(request):
    context={'Name':'Shahin'}
    return render(request,'about.html',context)