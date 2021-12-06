from django.db.models.aggregates import Sum
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from . import models


@receiver(post_save, sender=models.Projetos)
def teste_projeto(sender, instance, created, **kwargs):
    print("====================signal=============================")
    