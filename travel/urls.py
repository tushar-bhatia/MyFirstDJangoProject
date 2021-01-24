from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('tours', views.tours, name="tours"),
    path('offers', views.offers, name="offers"),
    path('contacts', views.contacts, name="contacts"),
    path('blog', views.blog, name="blog"),
    path('index', views.home, name="index"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)