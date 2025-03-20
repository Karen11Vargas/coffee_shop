from django.urls import reverse_lazy
from django.views import generic

from .models import Product
from .forms import ProductForm
# Create your views here.
class ProductFormView(generic.FormView):
    
    # Nombre del template
    template_name = "products/add_product.html"
    # Importar el formulario que renderizara 
    form_class = ProductForm
    # La url que redireccionara al finalizar la peticion
    success_url =  reverse_lazy('list_product')
    
    # Funcion que validara el formulario que se envie 
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"