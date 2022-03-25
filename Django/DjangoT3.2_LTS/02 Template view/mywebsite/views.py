from django.views.generic.base import TemplateView


# inheritence dari TemplateResponseMixin
# ContexMixin
# View
class IndexView(TemplateView):
    pass


class ParameterView(TemplateView):
    template_name = "parameter.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # context = kwargs
        context["judul"] = "Home parameter"
        context["penulis"] = "Khadafi"
        return context


class ContextView(TemplateView):
    template_name = "context.html"

    def get_context_data(self):
        context = {
            "judul": "Home Context",
            "penulis": "Khadafi",
        }
        return context
