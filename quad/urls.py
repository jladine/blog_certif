from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from forms import MyRegistrationForm
from views import HomepageView, RegistrationView, DashboardView, ArticleUpdateView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^register$', RegistrationView.as_view(form_class=MyRegistrationForm), name='registration_register'),
    url(r'^accounts/', include('registration.auth_urls')),
    url(r'^backoffice/$', DashboardView.as_view(), name='backoffice'),
    url(r'^backoffice/update/article/(?P<slug>[\w-]+)$', ArticleUpdateView.as_view(), name='update_article'),


]
