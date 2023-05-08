from django.urls import path
from store.views import index, product_detail, carte, delete_cart, voir_panier, valid_command, voir_command, voir_categorie


urlpatterns = [
                  path('', index, name='index'),
                  path('product/<str:slug>', product_detail, name="productss"),
                  path('category/',voir_categorie, name="category"),
                  path('cart/', carte, name="carter"),
                  path('voirpanier/<str:slug>', voir_panier, name="voir-panier"),
                  path('voircommand/',voir_command, name="voir-command"),
                  path('validcommand/', valid_command, name="valid"),
                  path('orders/delete/<int:order_id>', delete_cart, name="delete-cart"),
]    