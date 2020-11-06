from django.shortcuts import render
from core.erp.models import Category, Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class  CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = cat.name
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)    

    # con este metodo modificamos la consulta 
    # def get_queryset(self):
    #     return Category.objects.filter(name__startswith='b')


    # devuelve un diccionario y podemos pasarle mas variables a nuestro contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context        