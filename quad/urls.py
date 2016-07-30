from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from forms import MyRegistrationForm
from views import homepage, RegistrationView

urlpatterns = [
    url(r'^register$', RegistrationView.as_view(form_class=MyRegistrationForm), name='registration_register'),
    url(r'^accounts/', include('registration.auth_urls')),
    url(r'^$', homepage),
    
]
