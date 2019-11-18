from django.contrib import admin
from django.urls import (
    include,
    path
)
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='contemplate/')),
    path('admin/', admin.site.urls),
    path('contemplate/', include('contemplate.urls'))
]
