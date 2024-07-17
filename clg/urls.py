from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('form/', views.form, name="collage"),
    path('table/', views.table, name="table"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
