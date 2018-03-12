from django.shortcuts import render
from . import forms
from .models import Data

# Create your views here.

# Helper functions
#database columns --> name, a = type_of, b = brand_obj, c = brand_sent, d = seg

def return_data(a,b,c,d):
    if a is None and b is None and c is None and d is None:
        return Data.objects.values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif a is not None and b is None and c is None and d is None:
        return Data.objects.filter(type_of__icontains = a).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif b is not None and a is None and c is None and d is None:
        return Data.objects.filter(brand_obj__icontains = b).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif c is not None and a is None and b is None and d is None:
        return Data.objects.filter(brand_sent__icontains = c).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif d is not None and a is None and b is None and c is None:
        return Data.objects.filter(seg__icontains = d).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif a is not None and b is not None and c is None and d is None:
        return Data.objects.filter(type_of__icontains = a, brand_obj__icontains = b).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif a is not None and c is not None and b is None and d is None:
        return Data.objects.filter(type_of__icontains = a, brand_sent__icontains = c).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif a is not None and d is not None and b is None and c is None:
        return Data.objects.filter(type_of__icontains = a, seg__icontains = d).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif b is not None and c is not None and a is None and d is None:
        return Data.objects.filter(brand_obj__icontains = b, brand_sent__icontains = c).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif b is not None and d is not None and a is None and c is None:
        return Data.objects.filter(brand_obj__icontains = b, seg__icontains = d).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif c is not None and d is not None and a is None and b is None:
        return Data.objects.filter(brand_sent__icontains = c, seg__icontains = d).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif a is not None and b is not None and c is not None and d is None:
        return Data.objects.filter(type_of__icontains = a, brand_obj__icontains = b, brand_sent__icontains = c).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif a is not None and b is not None and d is not None and c is None:
        return Data.objects.filter(type_of__icontains = a, brand_obj__icontains = b, seg__icontains = d).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif a is not None and c is not None and d is not None and b is None:
        return Data.objects.filter(type_of__icontains = a, brand_sent__icontains = c, seg__icontains = d).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    elif b is not None and c is not None and d is not None and a is None:
        return Data.objects.filter(brand_obj__icontains = b, brand_sent__icontains = c, seg__icontains = d).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')
    else:
        return Data.objects.filter(type_of__icontains = a, brand_obj__icontains = b, brand_sent__icontains = c, seg__icontains = d).values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')


def index(request):
    form = forms.users_filter()
    u = Data.objects.values_list('name', 'image','type_of', 'brand_obj', 'brand_sent', 'seg')


    # Form check
    if request.method == 'POST':
        form = forms.users_filter(request.POST)
        u = Data.objects.values_list('name','image','type_of', 'brand_obj', 'brand_sent', 'seg')


        if form.is_valid():
            a = form.cleaned_data['type_filter']
            b = form.cleaned_data['objective_filter']
            c = form.cleaned_data['sentiment_filter']
            d = form.cleaned_data['segment_filter']


            u = return_data(a,b, c, d)
            return render(request,'filter_app/index.html',{'form':form , 'datatable' : u,})





    return render(request,'filter_app/index.html',{'form':form , 'datatable' : u})
