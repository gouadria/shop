from django.urls import path
from accounts.views import signup, logout_user, loguin

urlpatterns = [
                  path('signup/', signup, name='signup'),
                  path('login/', loguin, name='login'),
                  path('logout/', logout_user, name='logout'),
]                  