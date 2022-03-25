from django.views.generic import TemplateView

# from schl.views import ArtikelPerkategori

# class BlogHomeView(TemplateView, ArtikelPerkategori):
#     template_name = "index.html"

#     def get_context_data(self):
#         queryset = self.get_latest_artikel_each_kategori()
#         context = {
#             "latest_artikel_list": queryset,
#         }
#         return context

# PROFIL
class SejarahView(TemplateView):
    template_name = "profil/sejarah.html"

    def get_context_data(self):
        context = {
            "page_title": "Sejarah",
        }
        return context


class SambutanView(TemplateView):
    template_name = "profil/sambutan.html"

    def get_context_data(self):
        context = {
            "page_title": "Sambutan",
        }
        return context


class FasilitasView(TemplateView):
    template_name = "profil/fasilitas.html"

    def get_context_data(self):
        context = {
            "page_title": "Beranda",
        }
        return context


# BERANDA
class BerandaView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = {
            "page_title": "Beranda",
        }
        return context
