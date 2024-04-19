from django.urls import path
from articles import views

urlpatterns = [
    path("", views.articles, name="articles"),
    path("new/", views.new, name = "new"),
    path("create/", views.create, name = "create"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update")
]