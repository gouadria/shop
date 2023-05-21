from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from store.models import Product, cart, order, command, Article, category, Publicite
from django.utils import timezone
from django.contrib import messages



def index(request):
    products = Product.objects.all()
    Category = category.objects.get(name='pc portable')
    productcs = Product.objects.filter(category__name='pc portable')
    Category = category.objects.get(name='smartphone')
    prod =  Product.objects.filter(category__name='smartphone')
    Category = category.objects.get(name='tv')
    prods =  Product.objects.filter(category__name='tv')
    producty = Product.objects.get(name='BENCOY11')
    publicites = Publicite.objects.all()
    if request.method=="POST":
      item_name = request.POST.get('item-name')
      if item_name != "" and item_name is not None:
        productcs = Product.objects.filter(name__icontains=item_name)
    
    
    user = request.user  
    Cart = None     
    if request.user.is_authenticated:
        try:
            Cart = request.user.cart
            Orderss = Cart.orders.all()
            Total = 0
            for order in Orderss:
                Total += order.quantity * order.product.price
            context1= {"orderss": Orderss}
            context2 = {"products": products}
            context3 = {"productcs": productcs}
            context5 = {"prodsss":prod}
            context6 = {"prodss":prods}
            context7 = {"productt":producty}
            context4 = {"Total":Total}
            context8 = {"publicites":publicites}
            context = {**context1,**context2,**context3,**context4,**context5,**context6,**context7,**context8}
            return render(request, 'store/index.html', context)
        except cart.DoesNotExist: 
            pass    
            
    context2 = {"products": products}
    context3 = {"productcs": productcs}
    context5 = {"prodsss":prod}
    context6 = {"prodss":prods}
    context7 = {"productt":producty}
    context = {**context2,**context3,**context5,**context6,**context7}
    return render(request, 'store/index.html', context)
def voir_categorie(request):
    if request.method == "POST":
        Products = Product.objects.all()
        category_name = request.POST.get('categorie')
        Category = category.objects.get(name=category_name)
        prod = Product.objects.filter(category__name= category_name)
        context1 = {"prod":prod}
        context2 = {"category_name":category_name}
        context = {**context1,**context2}
        return render(request, 'store/categorie.html',context)
    


def product_detail(request, slug):
    product = get_object_or_404(Product,slug=slug)
    if request.user.is_authenticated:
        try:
          Cart = request.user.cart
          if Cart:
           Total = 0
           TQTE = 0
           Orders = Cart.orders.all()
           for Order in Orders:
              TQTE += Order.quantity
              prix = Order.product.price
              Total += prix * Order.quantity
           context1 = {"orderss": Orders.all()}
           context2 = {"Total": Total}
           context3 = {"TQTE": TQTE}
           context4 = {"Cart":Cart}
           context5 = {"product":product}
           context =  {**context1,**context2,**context3,**context4,**context5}
           return render(request, "store/detail.html", context)
        except cart.DoesNotExist: 
          pass
    context = {
            'product': product,
            'user': request.user.is_authenticated,
    }
            
    return render(request, "store/detail.html", context)




def carte(request):
    Cart = get_object_or_404(cart, user=request.user)
    orders = Cart.orders.all()
    Total = 0
    for order in orders :
        Total += order.quantity * order.product.price 
        
    return render(request, "store/cart.html", context={"orders": Cart.orders.all(),"Total":Total})


def delete_cart(request, order_id):
    Order = get_object_or_404(order,id=order_id)
    if Order:
        product = Order.product
        quantite = Order.quantity
        Order.delete()
    return redirect('index')

def voir_panier(request,slug):
     user = request.user
     product = get_object_or_404(Product,slug=slug)
     if request.method == "POST":
        qte = request.POST.get("QTE")
        if qte != 0:
          Cart, _ = cart.objects.get_or_create(user=user)
          Order, created = order.objects.get_or_create(user=user, ordered=False, product=product)
          Order.quantity = qte
          Order.save()
          Cart.orders.add(Order)
          Cart.save()
     Cart = get_object_or_404(cart, user=user)
     Total = 0
     TQTE = 0
     Orders = Cart.orders.all()
     for Order in Orders:
       TQTE += Order.quantity
       prix = Order.product.price
       Total += prix * Order.quantity
     context1 = {"orderss": Orders.all()}
     context2 = {"Total": Total}
     context3 = {"TQTE": TQTE}
     context4 = {"Cart":Cart}
     context5 ={"product":product}
     context = {**context1, **context2, **context3,**context4,**context5}
     return render(request, "store/detail.html", context)
def voir_command(request):
    user=request.user
    Cart, _ = cart.objects.get_or_create(user=user)
    Total = 0
    TQTE = 0
    Orders = Cart.orders.all()
    for Order in Orders:
       TQTE += Order.quantity
       prix = Order.product.price
       Total += prix * Order.quantity
    context1 = {"orderss": Orders.all()}
    context2 = {"Total": Total}
    context3 = {"TQTE": TQTE}
    context = {**context1, **context2, **context3}
    return render(request, "store/voir-command.html", context)
    
    
def valid_command(request):
    user = request.user
    if request.method == 'POST':
        email = request.POST['email']
        Address = request.POST['Address']
        pays = request.POST['pays']
        city = request.POST['city']
        zip = request.POST['zip']
        Cart = get_object_or_404(cart, user=user)
        orders = Cart.orders.all()
        Total = 0
        nbre = 0
        Command, _ = command.objects.get_or_create(user=user, email=email, Address=Address, pays=pays, city=city, zip=zip, Cart=Cart, Total_command=Total, Nbre_Article=nbre)
        for Order in orders:
          Article_name = Order.product.name
          Article_qtite = Order.quantity
          if Article_qtite > Order.product.stock:
             message = ' le quantite demandé est superieur à quantité en stock de la : ' + Article_name + ' \nquantite en stock est : ' + str(Order.product.stock)
             messages.add_message(request, messages.ERROR, message, extra_tags='alert-danger')
             return redirect('index')
          Articles = Article(Command=Command, name=Article_name, quantite=Article_qtite)
          Total += Order.quantity * Order.product.price
          Order.ordered = True
          Order.product.stock = Order.product.stock - Order.quantity
          Articles.save()
          Order.product.save()
          nbre += 1
        Command.Nbre_Article = nbre
        Command.Total_command = Total
        Command.date_command = timezone.now()
        Command.save()
        Cart.orders.all().delete()
        return render(request, "store/validation.html", context={"user": user})
    return redirect('voir-command')


    