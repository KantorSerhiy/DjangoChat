from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from users.forms import CustomUserForm


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:index')

        form = CustomUserForm()
        return render(request, 'registration/register.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        form = CustomUserForm(request.POST or None)
        if form.is_valid():
            # Model Form Returns the object created
            user = form.save()
            login(request, user)
            return redirect('')

        return render(request, 'registration/register.html', {
            'form': form
        })

def index(request):
    return render(request, "index.html")