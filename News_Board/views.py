from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View

from news.models import Post, Comment

from news.forms import CommentForm


def home(request):

    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, "base.html", ctx)


def upvote(request, id):
    try:
        post = Post.objects.get(pk=id)
        post.upvotes += 1
        post.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('home')


class Comments(View):

    model = Comment
    form_model = CommentForm
    template = "comments.html"

    def get(self, request, id):
        comments = self.model.objects.all().filter(post=id)
        ctx = {'comments': comments, 'id': id, 'form': self.form_model}
        return render(request, self.template, ctx)

    def post(self, request, id):
        form = self.form_model(request.POST or None)
        comments = self.model.objects.all().filter(post=id)
        if form.is_valid():
            comment = form.save()
            comment.refresh_from_db()
            comment.author = form.cleaned_data.get('author')
            comment.content = form.cleaned_data.get('content')
            comment.post = form.cleaned_data.get('post')
            comment.save()
            ctx = {'comments': comments, 'id': id, 'form': form}
            return render(request, self.template, ctx)
        else:
            ctx = {'comments': comments, 'id': id, 'form': form}
            return render(request, self.template, ctx)
