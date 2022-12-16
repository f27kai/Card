from django.shortcuts import render, redirect, HttpResponse
from .models import (
    Card,
    Card_type,
)

from .forms import CardForm

def index(request):
    cards = Card.objects.all()

    context = {
        'cards': cards,
    }

    return render(request, 'main/index.html', context)


def informations(request, pk):
    info = Card.objects.get(pk=pk)


    context = {

        'info': info,
    }

    return render(request, 'main/information.html', context)

def create_card(request):
    if request.method == 'POST':
        form = CardForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CardForm()

        context = {
            'form': form
        }
        return render(request, 'main/create.html', context)


def update_card(request, pk):
    post = Card.objects.get(pk=pk)
    if request.method == "POST":
        post = CardForm(request.POST, instance=post)
        if post.is_valid():
            post.save()
            return redirect('index')
        else:
            return HttpResponse('Ошибка')
    else:
        form = CardForm(instance=post)

    context = {
        'form': form
    }
    return render(request, 'main/update.html', context)


def delete_card(request, pk):
    post = Card.objects.get(pk=pk)
    post.delete()
    return redirect('index')

def get_viza(request):
    card_type = Card_type.objects.get(pk=1)

    viza = Card.objects.filter(card_type = card_type)

    context = {
        'viza': viza
    }

    print(viza)

    return render(request, 'main/viza.html', context)


def get_elkart(request):
    card_type = Card_type.objects.get(pk=2)

    elkart = Card.objects.filter(card_type = card_type)

    context = {
        'elkart': elkart
    }

    print(elkart)

    return render(request, 'main/elkart.html', context)