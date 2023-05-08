from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render




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
    logout(request)
    return redirect("index")


def loguin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

    return render(request, "account/login.html")


def your_views(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'account/login.html')


