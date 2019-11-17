from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView


class SignIn(FormView):
    def get(self, request, *args, **kwargs):
        return render(request, 'sign_in.html')


class SignUp(FormView):
    def get(self, request, *args, **kwargs):
        return render(request, 'sign_up.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=200)


class SignOut(FormView):
    def get(self, request, *args, **kwargs):
        return render(request, 'sign_out.html')
