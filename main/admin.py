from django.contrib import admin
from .models import (
    Card,
    Card_type,
)

admin.site.register(Card)
admin.site.register(Card_type)