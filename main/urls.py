from django.urls import path
from .views import (
    index,
    informations,
    create_card,
    update_card,
    delete_card,
    get_viza,
    get_elkart,
)

urlpatterns = [
    path('index/', index, name='index'),
    path('informations/<int:pk>', informations, name='informations'),
    path('create/', create_card, name='create'),
    path('update/<int:pk>', update_card, name='update'),
    path('delete/<int:pk>', delete_card, name='delete'),
    path('viza/', get_viza, name='viza'),
    path('elkart/', get_elkart, name='elkart'),

]

