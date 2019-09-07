from django.shortcuts import render, get_object_or_404
from .models import Character, Card

def gallery(request):

    all_list = {"card_list": Card.objects.all(),
                "character_name": Character.objects.all(),
    }
    return render(request, 'gallery/gallery.html', all_list)

def chara_card(request, pk):
    all_list = {"character_filter": get_object_or_404(Character, pk=pk),
            "card_list": Card.objects.filter(card_character=pk),
            "character_name": Character.objects.all(),
            "pk": pk,
    }
    return render(request, 'gallery/chara_card.html', all_list)
