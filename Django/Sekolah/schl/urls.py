from django.urls import path, re_path

from .views import ArtikelListView

app_name = "schl"
urlpatterns = [
    re_path(r"^$", ArtikelListView.as_view(), name="list"),
]
