from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from .views import BerandaView, FasilitasView, SambutanView, SejarahView

urlpatterns = [
    # path("sekolah/", include("schl.urls", namespace="schl")),
    # Profil
    path("profil/sambutan", SambutanView.as_view(), name="sambutan"),
    path("profil/sejarah", SejarahView.as_view(), name="sejarah"),
    path("profil/fasilitas", FasilitasView.as_view(), name="fasilitas"),
    # Beranda
    path("", BerandaView.as_view(), name="home"),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
