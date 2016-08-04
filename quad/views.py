from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy
from registration import signals
from registration.views import RegistrationView as BaseRegistrationView
from django.contrib.auth import authenticate, get_user_model, login
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, TemplateView

from models import *
from forms import ArticleForm, CommentForm

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

class ArticleCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('quad.can_add_article','quad.can_change_article', 'quad.can_delete_article')
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

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail_article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comments'] = self.get_object().comment_set.all()
        context['form'] = CommentForm
        return context

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.kwargs['article_id'])
        return context

    def get_form_kwargs(self):
        form_kwargs = super(CommentCreateView, self).get_form_kwargs()
        form_kwargs.update({
            "initial" : {
                "author" : self.request.user.profil,
                "article" : self.kwargs['article_id']
            }
        })
        return form_kwargs

    def form_valid(self, form):
            form.save()
            return super(CommentCreateView, self).form_valid(form)

class UserDetailView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleDetailView, self).get_context_data(**kwargs)
    #     context['comments'] = self.get_object().comment_set.all()
    #     context['form'] = CommentForm
    #     return context

class UserUpdateView(UpdateView):
    model = User
    fields = ["email", "username", "last_name", "first_name"]
    template_name = 'update_user.html'
    success_url = reverse_lazy('homepage')
