from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from news.models import Post, Comment, Author

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
    authors = Author.objects.all()
    template = "comments.html"

    def get(self, request, id):
        comments = self.model.objects.all().filter(post=id)
        ctx = {'comments': comments, 'id': id, 'authors': self.authors}
        return render(request, self.template, ctx)

    def post(self, request, id):
        # post_obj = get_object_or_404(Post, id=id)
        form = self.form_model(request.POST or None)
        comments = self.model.objects.all().filter(post=id)

        if form.is_valid():
            form.save()
            return render(request, self.template, context={'comments': comments})
        else:
            return render(request, self.template, context={'comments': comments, 'id': id, 'form': form, 'authors': self.authors})
