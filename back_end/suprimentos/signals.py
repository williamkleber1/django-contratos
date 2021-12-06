from django.db.models.aggregates import Sum
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from . import models

@receiver(pre_save, sender=models.Projetos)
def teste_projeto_pre(sender, instance, **kwargs):
    print("====================post save signal=============================")


@receiver(post_save, sender=models.Projetos)
def teste_projeto_post(sender, instance, created, **kwargs):
    print("====================post save signal=============================")