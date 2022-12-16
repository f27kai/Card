from django.db import models


class Card_type(models.Model):
    type = models.CharField(max_length=60)

    def __str__(self):
        return self.type

class Card(models.Model):
    cardholder_name = models.CharField(max_length=160)
    number = models.CharField(max_length=19)
    expiry_date = models.CharField(max_length=5)
    CVV = models.CharField(max_length=3)
    card_type = models.ForeignKey(Card_type, on_delete=models.CASCADE)


    def __str__(self):
        return self.cardholder_name
