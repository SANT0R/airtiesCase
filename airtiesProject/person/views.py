from django.shortcuts import render
from person.models import person

# Create your views here.



def persons(request):


  
    persons = person.objects.all()    #pull the DB
    


    #Dictionary structure to send html template 
    context = {
        "persons":persons,
    }

    return render(request,'index.html',context)