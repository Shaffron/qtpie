from django.urls import path
from contemplate.views import Contemplate

urlpatterns = [
    path('<int:today>', Contemplate.as_view(), name='today-contemplate')
]
