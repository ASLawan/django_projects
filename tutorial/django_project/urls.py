from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("", include("blog.urls")),
    path("users/", include("users.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)