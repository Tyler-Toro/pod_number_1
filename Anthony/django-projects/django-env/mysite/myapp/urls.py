from django.urls import path
from myapp.views import hello
from myapp.views import goodbye

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    # myapp/<str:name>
    path('<str:name>', hello, name='hello_name'),
]

urlpatterns2 = [
    # myapp/goodbye/django
    path('', goodbye, name='goodbye'),
    # myapp/<str:name>
    path('<str:name>', goodbye, name='goodbye_name'),
]