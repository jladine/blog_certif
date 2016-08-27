from django.conf.urls import url, include
from django.views.decorators.http import require_POST
from forms import MyRegistrationForm
from views import *

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^register$', RegistrationView.as_view(form_class=MyRegistrationForm), name='registration_register'),
    url(r'^accounts/', include('registration.auth_urls')),
    url(r'^backoffice/$', DashboardView.as_view(), name='backoffice'),
    url(r'^backoffice/create/article', ArticleCreateView.as_view(), name='create_article'),
    url(r'^backoffice/update/article/(?P<slug>[\w-]+)$', ArticleUpdateView.as_view(), name='update_article'),
    url(r'^backoffice/delete/article/(?P<slug>[\w-]+)$', ArticleDeleteView.as_view(), name='delete_article'),
    url(r'^article/(?P<slug>[\w-]+)$', ArticleDetailView.as_view(), name='detail_article'),
    url(r'^comment/(?P<article_id>\d+)/$', CommentCreateView.as_view(), name='create_comment'),

    url(r'^compte/(?P<pk>\d+)$', UserDetailView.as_view(), name='compte'),
    url(r'^compte/update/(?P<pk>\d+)$', UserUpdateView.as_view(), name='user_update'),

]
