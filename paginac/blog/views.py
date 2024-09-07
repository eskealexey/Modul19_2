from django.db.models.sql.datastructures import Empty
from django.shortcuts import render
from django.template.defaultfilters import title
from .models import Posts
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    SELECT_CHOUIS = ['3', '5', '10']
    title_ = 'Главная'
    posts = Posts.objects.all()

    if request.GET.get('pag') is None:
        pag = 3
    else:
        pag = request.GET.get('pag')

    if request.method == 'POST':
        select = request.POST.get('select')
        if select is None:
            pag = 3
        else:
            pag = select


    paginator = Paginator(posts, pag)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title_,
        'page_obj': page_obj,
        'select_chouis': SELECT_CHOUIS,
        'pag': pag,
    }
    return render(request, 'index.html', context=context)
