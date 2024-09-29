from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('groq-query/',views.groq_query,name='groq-query'),
]