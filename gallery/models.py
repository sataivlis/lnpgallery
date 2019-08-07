from django.db import models
from django.conf import settings

# table that contains 4 character's name;
# LZXB - 1.李泽言 2.周棋洛 3.许墨 4.白起
class Character(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Card(models.Model):
    card_character = models.ForeignKey(Character, on_delete=models.CASCADE)
    card_title = models.CharField(max_length=10)
    img_url = models.TextField()

    def __str__(self):
        return self.card_title
