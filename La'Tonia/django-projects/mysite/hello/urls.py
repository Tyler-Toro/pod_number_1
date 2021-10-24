from django.urls import path
from hello.views import hello, hello_name, goodbye, you_there, stay

urlpatterns = [
    path('', hello, name='hello'),
    path('<str:name>/', hello_name, name='hello_name'),
    path('goodbye/<str:name>', goodbye, name='name'),
    path('you_there/<str:name>', you_there, name='name'),
    path('stay/<str:name>', stay, name='name'),
]