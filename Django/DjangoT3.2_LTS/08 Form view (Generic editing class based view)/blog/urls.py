from django.urls import path, re_path
from django.views.generic import DetailView, FormView, ListView

from .forms import ArtikelForm
from .models import Artikel
from .views import ArtikelDetailView, ArtikelFormView, ArtikelListView

app_name = "blog"
urlpatterns = [
    re_path(
        r"^create/$",
        ArtikelFormView.as_view(),
        name="create",
    ),
    re_path(
        r"^(?P<penulis>\w+)/(?P<page>\d+)$",
        ArtikelListView.as_view(),
        name="list",
    ),
    re_path(
        r"^(?P<penulis>\w+)/$",
        ArtikelListView.as_view(),
        name="list",
    ),
    re_path(
        r"^detail/(?P<slug>[\w-]+)$",
        ArtikelDetailView.as_view(),
        name="detail",
    ),
    # re_path(
    #     r"^detail/(?P<slug>[\w-]+)$",
    #     DetailView.as_view(model=Artikel),
    #     name="detail",
    # ),
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
