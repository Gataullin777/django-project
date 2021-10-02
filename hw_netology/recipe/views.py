from django.http import HttpResponse
from django.shortcuts import render

def main_menu(request):
    return render(request, template_name='recipe/welcome.html', context={})

def repice(request, dish):
    persons_count = int(request.GET.get('servings', 1))

    DATA = {
        'omlet': {
            'яйца, шт': 2 * persons_count,
            'молоко, л': 0.1 * persons_count,
            'соль, ч.л.': 0.5 * persons_count,
                },
        'pasta': {
            'макароны, г': 0.3 * persons_count,
            'сыр, г': 0.05 * persons_count,
                },
        'buter': {
            'хлеб, ломтик': 1 * persons_count,
            'колбаса, ломтик': 1 * persons_count,
            'сыр, ломтик': 1 * persons_count,
            'помидор, ломтик': 1 * persons_count,
                }

                    }

    value = ''
    if dish == 'omlet':
        value = DATA['omlet']

    elif dish == 'pasta':
        value = DATA['pasta']

    elif dish == 'buter':
        value = DATA['buter']

    context = {'dict': value}
    return render(request, template_name='recipe/index.html', context=context)