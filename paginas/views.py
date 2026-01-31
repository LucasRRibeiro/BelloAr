from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class MenuView(TemplateView):
    template_name = 'paginas/menu.html'
