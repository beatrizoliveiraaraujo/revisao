from dataclasses import fields
from turtle import update
from django.contrib import admin
from . import models
from django.contrib import messages
from django.utils.translation import ngettext

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'preco', 'verificar_estoque']
    list_editable = ['preco']
    list_filter = ['categoria']
    actions = ['zerar_estoque', 'estoque_baixo', 'estoque_ok', 'aumentar_10', 'descontar_10']

    def verificar_estoque(self, produto):
        if produto.qtd_estoque == 0:
            return "Estoque Zerado"
        if produto.qtd_estoque < 5:
            return "Estoque Baixo"
        if produto.qtd_estoque >= 5:
            return "Estoque Ok"

    def zerar_estoque(self, request, queryset):
        total = queryset.update(qtd_estoque=0)
        self.message_user(request, ngettext('%d produto do estoque foi atualizado com sucesso.', '%d produtos do estoque foi atulaizado com sucesso.', total,) % total, messages.SUCCESS)

    def estoque_baixo(self, request, queryset):
        total = queryset.update(qtd_estoque=4)
        self.message_user(request, ngettext('%d produto do estoque foi atualizado com sucesso.', '%d produtos do estoque foi atulaizado com sucesso.', total,) % total, messages.SUCCESS)

    def estoque_ok(self, request, queryset):
        total = queryset.update(qtd_estoque=5)
        self.message_user(request, ngettext('%d produto do estoque foi atualizado com sucesso.', '%d produtos do estoque foi atulaizado com sucesso.', total,) % total, messages.SUCCESS)

    def aumentar_10(self, request, queryset):
        for produto in queryset:
            preco_antigo = float(produto.preco)
            preco_novo = preco_antigo*1.10
            produto.preco = preco_novo
            produto.save(update_fields=['preco'])

    def descontar_10(self, request, queryset):
        for produto in queryset:
            preco_antigo = float(produto.preco)
            preco_novo = preco_antigo*0.90
            produto.preco = preco_novo
            produto.save(update_fields=['preco'])

@admin.register(models.Cliente)
class AdminCliente(admin.ModelAdmin):
    search_fields = ['nome__startswith']

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Categoria)
admin.site.register(models.Pedido)
admin.site.register(models.PedidoItem)


