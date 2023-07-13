from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('about', views.about, name='aboute'),
    path('item/<int:id>', views.get_item, name='item-detail'),
    path('items', views.items_list, name='items-list')
]
