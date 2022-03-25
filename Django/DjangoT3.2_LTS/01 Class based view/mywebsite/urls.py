from django.contrib import admin
from django.urls import path

from .views import IndexClassView, index

urlpatterns = [
    path("", index, name="home"),
    path(
        "class", IndexClassView.as_view(template_name="index.html"), name="home_class"
    ),
    path(
        "class2",
        IndexClassView.as_view(template_name="index2.html"),
        name="home_class2",
    ),
    path("admin/", admin.site.urls),
]
