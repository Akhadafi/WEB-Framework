from django.urls import path, re_path

from .views import (
    ArtikelCreateView,
    ArtikelDeleteView,
    ArtikelDetailView,
    ArtikelKategoriListView,
    ArtikelListView,
    ArtikelManageListView,
    ArtikelUpdateView,
)

app_name = "artikel"
urlpatterns = [
    re_path(r"^manage/update/(?P<pk>\d+)$", ArtikelUpdateView.as_view(), name="update"),
    re_path(r"^manage/delete/(?P<pk>\d+)$", ArtikelDeleteView.as_view(), name="delete"),
    re_path(r"^manage/$", ArtikelManageListView.as_view(), name="manage"),
    re_path(r"^tambah/$", ArtikelCreateView.as_view(), name="create"),
    re_path(
        r"^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$",
        ArtikelKategoriListView.as_view(),
        name="category",
    ),
    re_path(r"^detail/(?P<slug>[\w-]+)$", ArtikelDetailView.as_view(), name="detail"),
    re_path(r"^(?P<page>\d+)$", ArtikelListView.as_view(), name="list"),
]
