
from django.urls import path
from . import views
app_name = 'Shopping_app'


urlpatterns = [

    path('',views.All_Cat,name='All_Cat'),
    path('<slug:c_slug>',views.All_Cat,name='products_by_ category'),
    path('<slug:c_slug>/<slug:p_slug>', views.All_product, name='products'),

]
