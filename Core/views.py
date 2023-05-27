from django.shortcuts import render
from Product.models import Category,MotorCycle
# Create your views here.
def index(request):
    motos = MotorCycle.objects.filter(is_solder=False)
    cat = Category.objects.all()

    return render(request,'core/index.html',{
        'categories':cat,
        'motos':motos
    })

def contact(request):
    return render(request,"core/contact.html",{})