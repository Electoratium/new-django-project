from django.views.generic import TemplateView


from .forms import BaseForm
class BaseView(TemplateView):
    template_name = 'landing.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BaseForm
        return context