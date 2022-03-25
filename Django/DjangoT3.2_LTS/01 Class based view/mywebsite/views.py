from django.shortcuts import render
from django.views import View


def index(request):
    context = {
        "judul": "Home",
    }
    if request.method == "POST":
        context["judul"] = "POST function based view"
    return render(request, "index.html", context)


class IndexClassView(View):
    template_name = ""
    context = {}
    # override method get dari parent class View
    def get(self, request):
        self.context["judul"] = "GET class based view"
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.context["judul"] = "POST class based view"
        return render(request, self.template_name, self.context)
