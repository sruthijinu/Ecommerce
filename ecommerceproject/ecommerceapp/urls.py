from . import views
from django.urls import path
app_name='ecommerceapp'

urlpatterns = [
    path('',views.allprodcategory,name='allprodcategory'),
    path('<slug:c_slug>/',views.allprodcategory,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]