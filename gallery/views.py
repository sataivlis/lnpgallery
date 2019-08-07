from django.shortcuts import render
from .models import Character, Card

def gallery(request):
    card_list = Card.objects.all()

    return render(request, 'gallery/gallery.html', {"card_list" : card_list})
