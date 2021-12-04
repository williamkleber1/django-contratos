from django.contrib import admin
from . import models


class FornecedoresForm(admin.ModelAdmin):
    search_fields = ['razao_social', 'cnpj', 'email']
    #list_filter = ['razao_social']
    list_display = ['razao_social', 'email']
    readonly_fields = ['id_user_cad','id_user_alt']

    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        
        else:
            obj.id_user_cad = request.user

        obj.save()

admin.site.register(models.Fornecedores, FornecedoresForm)
admin.site.register(models.Ordens)
admin.site.register(models.Contratos)
admin.site.register(models.ItensContratos)
admin.site.register(models.Projetos)
admin.site.register(models.NaturezasDespesa)
admin.site.register(models.Vigencias)
admin.site.register(models.ItensOrdem)
