from django.urls import path
from django.views.generic import RedirectView

from account.views import (
    SignIn,
    SignUp,
    SignOut
)

urlpatterns = [
    path('', RedirectView.as_view(url='sign-in')),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
]
