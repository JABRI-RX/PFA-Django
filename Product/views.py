from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect
from Product.models import Item,Category
from Product.forms import NewItemForm,EditItemForm
# Create your views here.

def items(request):
    query = request.GET.get("query","")
    category_id = request.GET.get("category_id",0 )
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False) 
    if category_id:
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'product/products.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id)
    })
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


@login_required
def edit(request,pk):
    item = get_object_or_404(Item,pk=pk,creatd_by=request.user)
    print("I have not enter the post ")
    if request.method == "POST":
        print("I am before EditItemForm ")
        form = EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            print("the form is valided wtf ? ")
            form.save()

            return redirect('Product:detail',pk=item.id)
        else:
            print("something fucked up")
         
    else:
        form = EditItemForm(instance=item)
    return render(request,"product/form.html",{
        'form':form,
        'title':'Edit Item'
    })

@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,creatd_by=request.user)
    item.delete()
    return redirect('dashboard:index')
