from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView, TemplateView

from .views import HomeRedirectView, HomeUserView, HomeView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home_view"),
    path("random", RedirectView.as_view(pattern_name="index"), name="random"),
    path("home", RedirectView.as_view(url="/"), name="home"),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("admin/", admin.site.urls),
    re_path(
        r"^home/(?P<user>[\w]+)$",
        HomeRedirectView.as_view(),
        name="home_redirect",
    ),
    re_path(
        r"^(?P<user>[\w]+)$",
        HomeUserView.as_view(),
        name="user",
    ),
]
