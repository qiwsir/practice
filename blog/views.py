from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from django.core.urlresolvers import reverse

from models import Article

from django.http import Http404

from forms import ArticlePublishForm

class ArticleListView(ListView):
    template_name = "blog_index.html"

    def get_queryset(self, **kwargs):
        object_list = Article.objects.all().order_by(F('created').desc())[:100]
        paginator = Paginator(object_list, 2)
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return object_list

class ArticlePublishView(FormView):
    template_name = "article_publish.html"
    form_class = ArticlePublishForm

    success_url = '/blog/'

    def form_valid(self, form):
        form.save(self.request.user.username)
        return super(ArticlePublishView, self).form_valid(form)

class ArticleDetailView(DetailView):
    template_name = "article_detail.html"

    def get_object(self, **kwargs):
        title = self.kwargs.get('title')
        try:
            article = Article.objects.get(title=title)
            article.views += 1
            article.save()
            article.tags = article.tags.split()
        except Article.DoesNotExist:
            raise Http404("Article does not exist.")
        return article

class ArticleEditView(FormView):
    template_name = "article_publish.html"
    form_class = ArticlePublishForm
    article = None

    def get_initial(self, **kwargs):
        title = self.kwargs.get("title")
        try:
            self.article = Article.objects.get(title=title)
            initial = {
                "title" : title,
                "content": self.article.content_md,
                "tags": self.article.tags,
            }
            return initial
        except Article.DoesNotExist:
            raise Http404("Article does not exist.")

    def form_valid(self, form):
        form.save(self.request, self.article)
        return super(ArticleEditView, self).form_valid(form)

    def get_success_url(self):
        title = self.request.POST.get('title')
        success_url = reverse('article_deatil', args=(title,))
        return success_url

def blog_index(request):
    context = {
        "test": "just for test.",
        "welcome": "hello world",
    }

    return render(request, "blog_index.html", context)
