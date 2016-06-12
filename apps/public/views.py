from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    template_name = 'base.html'
