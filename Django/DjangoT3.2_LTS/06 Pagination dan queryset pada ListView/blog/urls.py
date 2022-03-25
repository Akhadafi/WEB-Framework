from django.urls import path, re_path
from django.views.generic import ListView

from .models import Artikel
from .views import ArtikelListView, index

app_name = "blog"
urlpatterns = [
    re_path(
        r"^(?P<penulis>\w+)/(?P<page>\d+)$",
        ArtikelListView.as_view(),
        name="list",
    ),
    re_path(
        r"^(?P<page>\d+)$",
        ArtikelListView.as_view(),
        name="list",
    ),
    # path(
    #     "",
    #     ArtikelListView.as_view(),
    #     name="list",
    # ),
    # path("", ListView.as_view(model=Artikel), name="list"),
]
