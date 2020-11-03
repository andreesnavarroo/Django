from django.shortcuts import render
from core.erp.models import Category, Product

from django.views.generic import ListView

def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class  CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # con este metodo modificamos la consulta 
    def get_queryset(self):
        return Category.objects.filter(name__startswith='b')


    # devuelve un diccionario y podemos pasarle mas variables a nuestro contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context        