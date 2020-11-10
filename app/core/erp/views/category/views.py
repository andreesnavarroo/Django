from django.shortcuts import render
from core.erp.models import Category, Product
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from core.erp.forms import CategoryForm
from django.urls import reverse_lazy
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
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name  = 'category/create.html'
    success_url  = reverse_lazy('erp:category_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                # form = CategoryForm(request.POST)
                form = self.get_form()
                data = form.save()                    
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)           
    #     print(request.POST)
    #     form = CategoryForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    # devuelve un diccionario y podemos pasarle mas variables a nuestro contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'add'
        return context

class CategoryUpdateView(UpdateView):        
    model = Category
    form_class = CategoryForm
    template_name  = 'category/create.html'
    success_url  = reverse_lazy('erp:category_list')
    
    def dispatch(self, request, *args, **kwargs):  
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
  
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                # form = CategoryForm(request.POST)
                form = self.get_form()
                data = form.save()                    
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'edit'
        return context




class CategoryDeleteView(DeleteView):        
    model = Category
    template_name  = 'category/delete.html'
    success_url  = reverse_lazy('erp:category_list')

            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        return context            