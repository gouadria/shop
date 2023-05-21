from django.contrib import admin

from store.models import Product, category, order, cart, command, Article, Publicite

admin.site.site_header = "shop"
admin.site.site_title = "Gouadria-shop"
admin.site.index_title = "manageur"
class Admincategorie(admin.ModelAdmin):
    list_display = ('name', 'date_ajout')


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'date_ajout')
    search_fields =('category__name',)
    list_editable =('price',)

class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'ordered')



class AdminCommand(admin.ModelAdmin):
    list_display = ('user', 'Nbre_Article', 'Total_command', 'date_command', 'email', 'Address')


class AdminArticle(admin.ModelAdmin):
    list_display = ('Command', 'name', 'quantite')


admin.site.register(Product, AdminProduct)
admin.site.register(category, Admincategorie)
admin.site.register(order, AdminOrder)
admin.site.register(cart)
admin.site.register(command, AdminCommand)
admin.site.register(Article, AdminArticle)
admin.site.register(Publicite)