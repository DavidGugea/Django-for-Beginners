from django.urls import path
import views

urlpatterns = [
    path('', views.homePageView, name='home')
]
