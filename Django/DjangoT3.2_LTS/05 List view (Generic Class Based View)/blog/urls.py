from django.urls import path
from django.views.generic import ListView

from .models import Artikel
from .views import ArtikelListView, index

app_name = "blog"
urlpatterns = [
    path(
        "",
        ArtikelListView.as_view(),
        name="list",
    ),
    # path("", ListView.as_view(model=Artikel), name="list"),
]
