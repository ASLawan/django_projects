from django.urls import path
from users import views as auth_views

urlpatterns = [
    path("profile/", auth_views.user_profile, name="profile"),
    path("login/", auth_views.login_view, name="login"),
    path("logout/", auth_views.logout_view,  name="logout"),
]