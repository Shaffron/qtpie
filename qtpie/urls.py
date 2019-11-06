from django.contrib import admin
from django.urls import (
    include,
    path
)

import contemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contemplate/', include('contemplate.urls'))
]
