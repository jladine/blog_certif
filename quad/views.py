from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from registration.views import RegistrationView as BaseRegistrationView
from django.contrib.auth import authenticate, get_user_model, login
from registration import signals

User = get_user_model()

class RegistrationView(BaseRegistrationView):

    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user

    def get_success_url(self, user):
        return '/'


def homepage(request):
    return render(request,"homepage.html")
