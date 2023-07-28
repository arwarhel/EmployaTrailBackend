from django.urls import path
from .views import UserLogIn, UserRegister, UserLogOut

app_name = "user"

urlpatterns = [
    path('login', UserLogIn.as_view(), name="login"),
    path('register', UserRegister.as_view(), name="register"),
    path('logout', UserLogOut.as_view(), name="logout"),
]
