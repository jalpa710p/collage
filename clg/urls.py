from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form, name="collage"),
    path('table/', views.table, name="table"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
]
