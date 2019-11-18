from django.urls import path
from contemplate.views import (
    Contemplate,
    Ready,
    Sunday
)

urlpatterns = [
    path('', Contemplate.as_view(), name='contemplate-root'),
    path('<int:today>', Contemplate.as_view(), name='contemplate-today'),
    path('sunday', Sunday.as_view(), name='contemplate-sunday'),
    path('ready', Ready.as_view(), name='contemplate-ready')
]
