from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    context ={
        "name": 'Петров Николай Иванович',
        'email': 'my_mail@mail.ru'
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        'name': 'Евгений',
        'middle': 'Владимирович',
        'surname': 'Неупокоев',
        'phone': '8-123-456-67-89',
        'email': 'random_email@mail.ru'
        }
    context = {
        'author': author
    }
    return render(request, "about.html", context)



def get_item(request, id):
    """ По указанному id функция возвращает имя и кол-во через шаблон """

    try:
        item = Item.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Item with {id}=id not found')
        
    context = {'item': item}       
    return render(request, "item-page.html", context)    


def items_list(request):
    
    items = Item.objects.all()
    
    context = {
        "items": items
        }
    return render(request, "items-list.html", context)
