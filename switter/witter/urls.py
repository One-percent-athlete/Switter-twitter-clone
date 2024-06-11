from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile_list', views.profile_list, name="profile_list"),
    path('profile/<int:pk>', views.profile, name="profile"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('update_user', views.update_user, name="update_user"),
    path('register', views.register, name="register"),
    path('update_password/<int:pk>', views.update_password, name="update_password"),
    path('swit_like/<int:pk>', views.swit_like, name="swit_like"),
]
