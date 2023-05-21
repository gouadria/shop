from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from store.models import cart




User = get_user_model()








def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("index")


    return render(request, "account/signup.html")


def logout_user(request):
    if request.user.is_authenticated:
        try:
            Cart = request.user.cart
            Cart.delete()
        except cart.DoesNotExist:
            pass
    logout(request)
    return redirect("index")


def loguin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
         try:
            login(request, user)
            user.cart.delete()
            request.session['cart'] = {}  # Réinitialiser le panier de l'utilisateur
            return redirect("index")
         except cart.DoesNotExist:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, 'Invalid username or password.')

            return render(request, "account/login.html",{'error': 'Invalid username or password'})
    return render(request,"account/login.html")


