from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create_blog',views.create_blog),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete)
]