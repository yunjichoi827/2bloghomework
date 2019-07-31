
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('about', views.about, name="about"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
