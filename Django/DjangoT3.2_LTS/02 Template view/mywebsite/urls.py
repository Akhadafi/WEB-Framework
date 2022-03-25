from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import TemplateView

from .views import ContextView, IndexView, ParameterView

urlpatterns = [
    path("context/", ContextView.as_view()),
    path("default/", TemplateView.as_view(template_name="default.html")),
    path("", IndexView.as_view(template_name="index.html")),
    path("admin/", admin.site.urls),
    re_path(
        r"^parameter/(?P<parameter1>[0-9]+)/(?P<parameter2>[0-9]+)$",
        ParameterView.as_view(),
    ),
]

"""
    1. membuat class view di views.py, tetapi mengunakan templatenya
    2. jika halaman static,maka lakukan TemplateView pada urls.py
    3. membuat context saja, kita mengunakan class template view di views.py
    4. memasukan parameter kedalam template dengan mengunakan regex
"""
