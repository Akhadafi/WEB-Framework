from django.urls import path, re_path

from .views import SosmedDeleteView, SosmedFormView, SosmedListView

app_name = "sosmed"
urlpatterns = [
    path("create/", SosmedFormView.as_view(), name="create"),
    path("", SosmedListView.as_view(), name="list"),
    re_path(
        r"^updete/(?P<update_id>[0-9]+)/$",
        SosmedFormView.as_view(mode="update"),
        name="update",
    ),
    re_path(
        r"^delete/(?P<delete_id>[0-9]+)/$",
        SosmedDeleteView.as_view(),
        name="delete",
    ),
]
