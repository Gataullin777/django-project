from django.shortcuts import render, get_object_or_404
from phones.models import Phones


def show_catalog_view(request):
    sort = request.GET.get('sort', None)
    if sort is None:
        data = Phones.objects.filter().all()

    elif sort == 'name':
        data = Phones.objects.filter().order_by('name')

    elif sort == 'min_price':
        data = Phones.objects.filter().order_by('price')

    elif sort == 'max_price':
        data = Phones.objects.filter().order_by('-price')


    temp_list = []
    for i in data:
        temp_dict = {}
        temp_dict['name'] = i.name
        temp_dict['price'] = i.price
        temp_dict['image'] = str(i.image)
        temp_dict['slug'] = i.slug
        temp_list.append(temp_dict)
    template = 'catalog.html'
    context = {'data': temp_list}
    return render(request, template, context)


def show_product_view(request, slug):
    info_phones = get_object_or_404(Phones, slug=slug)
    template = 'product.html'
    context = {'info_phone': info_phones}
    return render(request, template, context)

