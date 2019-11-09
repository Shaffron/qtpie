from django.urls import path
from contemplate.views import Contemplate

urlpatterns = [
    path('<int:date>', Contemplate.as_view(), name='date-contemplate')
]
