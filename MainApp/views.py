from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


author = {
    'name': 'Евгений',
    'middle': 'Владимирович',
    'surname': 'Неупокоев',
    'phone': '8-123-456-67-89',
    'email': 'random_email@mail.ru'
}


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


# Create your views here.
def home(request):
    context ={
        "name": 'Петров Николай Иванович',
        'email': 'my_mail@mail.ru'
    }
    return render(request, "index.html", context)


def about(request):
#     result = f"""
# Имя: <b>{author["name"]}</b><br>
# Отчество: <b>{author["middle"]}</b><br>
# Фамилия: <b>{author["surname"]}</b><br>
# телефон: <b>{author["phone"]}</b><br>
# email: <b>{author["email"]}</b><br>
# <a href='/'> Home </a>
# """
#     return HttpResponse(result)
    context = {
        'author': author
    }
    return render(request, "about.html", context)


def get_item(request, id):
    """ По указанному id функция возвращает имя и кол-во через шаблон """
    for item in items:
        if item['id'] == id:
            # result = f"""
            # <h2>Имя: {item["name"]} </h2>
            # <p>Количество: {item["quantity"]}</p>
            # <a href='/item'> Назад </a>           
            # """
            # return HttpResponse(result)
            context = {
                'item': item
            }
            return render(request, "item-page.html", context)        
    return HttpResponseNotFound(f'Item with {id}=id not found')
    

def items_list(request):
    # result = "<h2>список товаров</h2><ol>"
    # for item in items:
    #     result += f"<li>{item['name']}</li>"
    # result += '</ol>'
    # return HttpResponse(result)
    context = {
        "items": items
        }
    return render(request, "items-list.html", context)
