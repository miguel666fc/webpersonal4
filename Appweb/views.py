from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,"Appweb/home.html")



def blog(request):
    return render(request,"Appweb/blog.html")
    
       
def contacto(request):
    return render(request,"Appweb/contacto.html")
      
