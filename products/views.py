from django.shortcuts import render
from .form import ProductForm 
from .models import Product

# Create your views here.
def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    data = {
        "obj": obj
    }
    return render(request,"products/detail.html",data)

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }        
    return render(request,'products/create_product.html', context)