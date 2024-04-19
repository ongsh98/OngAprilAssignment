from django.urls import path
from users import views

urlpatterns = [
    path("", views.users, name="users"),
    path("<str:username>/", views.profile, name="profile"),
]