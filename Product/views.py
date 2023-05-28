from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from Product.models import Item
from Product.forms import NewItemForm
# Create your views here.
def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]

    return render(request,'product/details.html',{
        'item':item,
        'related_items':related_items
    })
@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
             
            item.creatd_by = request.user
            item.save()

            return redirect('Product:detail',pk=item.id)
    form = NewItemForm()
    return render(request,"product/form.html",{
        'form':form,
        'title':'New Item'
    })