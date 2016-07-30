from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from registration.views import RegistrationView as BaseRegistrationView
from django.contrib.auth import authenticate, get_user_model, login
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, TemplateView

from models import *
from forms import ArticleForm

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


# def homepage(request):
#     return render(request,"homepage.html")

class HomepageView(ListView):
    model = Article
    template_name = 'homepage.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by("creation_date").filter(is_active = True)

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    # form_class = ArticleForm
    # success_url = reverse_lazy('creneau_montoir_previsonnel_list')

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['articles_on'] = Article.objects.filter(is_active = True)
        context['articles_off'] = Article.objects.filter(is_active = False)

        return context

class ArticleCreateView(CreateView):
    template_name = 'create_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('backoffice')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = "__all__"
    template_name = 'update_article.html'
    success_url = reverse_lazy('backoffice')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('backoffice')
