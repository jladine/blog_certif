from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from registration import signals
from django.db.models import Count, Prefetch
from registration.views import RegistrationView as BaseRegistrationView
from django.contrib.auth import authenticate, get_user_model, login
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, TemplateView

from models import *
from forms import ArticleForm, ArticleUpdateForm, CommentForm, LikeForm

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
    queryset = Article.objects.order_by("creation_date").filter(is_active = True)[::-1]
    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['popular_article'] = Article.objects.filter(is_active=True).annotate(vote_count=Count('comment')).order_by('-vote_count')[:2]
        context['articles'] = Article.objects.annotate(comment_count=Count('comment')).order_by('creation_date').filter(is_active=True).reverse()
        return context

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

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
    form_class = ArticleUpdateForm
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
        context['last_comments'] = self.get_object().comment_set.order_by("creation_date").reverse()[:3]
        context['pop_comments'] = self.get_object().comment_set.annotate(like_count=Count('like_set')).order_by('like_count').reverse()
        context['nb_comment'] = self.get_object().comment_set.count()
        context['last_article'] = Article.objects.order_by("creation_date").filter(is_active = True).reverse()[:5]
        # context['nb_like'] = like_count
        return context

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html'
    # success_url = reverse_lazy('create_comment')
    # def get_success_url(self, **kwargs):
    #     if  kwargs != None:
    #         return reverse_lazy('create_comment', kwargs = 1)
    #     else:
    #         return reverse_lazy('create_comment', args = 1)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CommentCreateView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)

        comments = {}
        for comment in Comment.objects.filter(article=self.kwargs['article_id']):
            comments[comment] = LikeForm({
                            'author': self.request.user,
                            'comment': comment
                            })
        context["object_list"] = comments
        return context

    def get_form_kwargs(self):
        form_kwargs = super(CommentCreateView, self).get_form_kwargs()
        form_kwargs.update({
            "initial" : {
                "author" : self.request.user,
                "article" : self.kwargs['article_id']
            }
        })
        return form_kwargs

    def form_valid(self, form):
            form.save()
            return super(CommentCreateView, self).form_valid(form)

    # def get_success_url(self, **kwargs):
    #     if  kwargs != None:
    #         return reverse_lazy('creation-comment', kwargs = {'id': kwargs[self.object.article.id]})

class UserDetailView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = self.object.id
        comment_like = self.object.like_set
        context['mycomments'] = Comment.objects.filter(author = user)
        context['mycommentslike'] = Comment.objects.annotate(like_count=Count('like_set')).filter(author = user).order_by('like_count').reverse()

        return context

class UserUpdateView(UpdateView):
    model = User
    fields = ["email", "username", "last_name", "first_name"]
    template_name = 'update_user.html'
    success_url = reverse_lazy('homepage')

class LikeFormView(FormView):
    form_class = LikeForm
    success_url = reverse_lazy('creation-comment')

    def form_valid(self, form):
            form.save()
            return super(LikeFormView, self).form_valid(form)
