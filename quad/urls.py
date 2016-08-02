from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from forms import MyRegistrationForm
from views import HomepageView, RegistrationView, DashboardView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^register$', RegistrationView.as_view(form_class=MyRegistrationForm), name='registration_register'),
    url(r'^accounts/', include('registration.auth_urls')),
    url(r'^backoffice/$', DashboardView.as_view(), name='backoffice'),
    url(r'^backoffice/create/article', ArticleCreateView.as_view(), name='create_article'),
    url(r'^backoffice/update/article/(?P<slug>[\w-]+)$', ArticleUpdateView.as_view(), name='update_article'),
    url(r'^backoffice/delete/article/(?P<slug>[\w-]+)$', ArticleDeleteView.as_view(), name='delete_article'),
    url(r'^article/(?P<slug>[\w-]+)$', ArticleDetailView.as_view(), name='detail_article'),

]
