from django.urls import path
from . import views
app_name = 'form'

urlpatterns = [
    path('form', views.form, name="form")

]