from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import FormView

from authentication.forms import LoginForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/home'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                print(user.is_authenticated)
                return redirect('home')
            messages.error(request, 'Email or password not correct')
        return render(request, 'login.html', {'form': form})
