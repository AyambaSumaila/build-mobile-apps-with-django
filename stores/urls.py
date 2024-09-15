from django.urls import path
from . import views

urlpatterns = [
    path('', views.PizzasListAPIView.as_view(), name='pizzas_list'),
    path('<int:id>/', views.PizzasRetrieveAPIView.as_view(), name='pizzas_detail'),
    path('create/', views.PizzasCreateAPIView.as_view(), name='pizzas_create'),
    path('update/<int:id>/', views.PizzasRetrieveUpdateAPIView.as_view(), name="pizzas_update"),
    path('delete/<int:id>/', views.PizzasDestroyAPIView.as_view(), name="pizzas_delete"),
    

]



