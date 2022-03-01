
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from .models import Product


def index(request):
    context ={}
    context["dataset"] = Product.objects.all()

    return render(request,'product/index.html', context)



def details(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
    context["range"] = range(1, context["data"].productquantity+1)
    return render(request, "product/details.html", context)

def quantity(request, id):

    quantityChose = request.POST.get('quantity')
    obj = get_object_or_404(Product, id = id)
    Product.objects.filter(id = id).update(productquantity = obj.productquantity - int(quantityChose))
    obj.refresh_from_db()
    return HttpResponseRedirect('/product')

   




