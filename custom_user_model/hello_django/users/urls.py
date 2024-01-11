from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("index", views.home, name="home"),
    path("", views.signup, name="signup"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("authors_and_sellers/", views.AuthorsAndSellersView, name="authors_and_sellers"),
    path("upload_files/", views.upload_files, name="upload_files"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
