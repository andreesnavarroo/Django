from django.urls import path

from core.erp.views.category.views import category_list, CategoryListView, CategoryCreateView

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    
]
