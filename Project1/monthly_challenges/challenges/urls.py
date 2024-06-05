from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number, name="monthly_challenge"),
    path("<str:month>", views.monthly_challenge, name="monthly_challenge_by_number"),
]