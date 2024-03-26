from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
dict = [
    ['Имя', 'Иван'],
    ['Отчество', 'Петрович'],
    ['Фамилия', 'Иванов'],
    ['телефон', '8-923-600-01-02'],
    ['email', 'vasya@mail.ru'],
]
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

itemsList = [[i['name'], f'item/{i["id"]}/'] for i in items]
def main(request):
    return HttpResponse("""<h1>"Изучаем django"</h1>
                             <strong>Автор</strong>:
                             <i>Иванов И.П.</i>""")

def about(request):
    return render(request, 'interface/about.html', context={'dict': dict})



def item(request, id):
    item = None
    for i in items:
        if int(i['id']) == int(id):
            item = i
    if item:
        return render(request, 'interface/item.html', context={'item':item})
    return HttpResponse(f'Товар с id={id} не найден')

def itemsPage(request):
    return render(request, 'interface/items.html', context={'items':itemsList})
