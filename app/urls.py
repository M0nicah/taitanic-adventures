from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
path('packages/', views.package_list, name+"package_list"),
]