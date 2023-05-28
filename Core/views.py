from django.shortcuts import render,redirect
from django.core.mail import send_mail
from Product.models import Category,Item
from Core.forms import SignUpForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:3]
    cats = Category.objects.all()
 
    return render(request,'core/index.html',{
        'cats':cats,
        'items':items
    })

def about(request):
    return render(request,"core/about.html",{})

def support(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        email= request.POST.get("email")
        SNM_mail = "jabri.salah65@gmail.com"
        desc = request.POST.get("desc")
        #send mail
        send_mail("Report From Customer : "+name,desc,email,(SNM_mail,),False)

    return render(request,"core/support.html",{'msg':msg})

def signup(request):
    form = ""
    if request.method == 'POST':
       
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        # return redirect('/login/')
    else:
         
        form = SignUpForm()
     
    return render(request, 'core/signup.html', {
        'form': form
    })