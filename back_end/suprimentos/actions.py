from django.utils.translation import ngettext
from django.contrib import messages



def atualiza_projeto(modeladmin, request, projetos):
    
    for projeto in projetos:
        projeto.titulo = "Teste action"
        projeto.save()
        
    modeladmin.message_user(request, ngettext(
        '%d Projetos foram atualizados.',
        '%d Projetos foram atualizados.',
        len(projetos),
        ) % len(projetos), messages.SUCCESS
    )
        
atualiza_projeto.short_description = "Atualizar projetos"
