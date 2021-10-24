from django.urls import path
from . import views

urlpatterns = [
    # sandwich home
    path('', views.sandwich, name='sandwich'),
    # sandwich/ingredients/<str:ingredient_type>
    # tried this w/o leading ingredients root route
    # path('ingredients/<str:ingredient_type>', views.ingredients_list, name = 'ingredients_list'),
    path('ingredients/<str:ingredient_type>', views.ingredients_list, name='ingredients_list'),
    # sandwich/random
    path('random', views.sandwich_generator, name = 'sandwich_generator'),
    path('full_menu', views.full_menu, name='full_menu'),
]