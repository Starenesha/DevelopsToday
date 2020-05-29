from django.db import models


class Author(models.Model):

    name = models.CharField(verbose_name='author', max_length=40)
    email = models.EmailField(verbose_name='e-mail')

    class Meta:
        db_table = 'author'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Post(models.Model):

    author = models.ForeignKey(Author, verbose_name='author', related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=80, blank=False)
    link = models.URLField(verbose_name='link', max_length=200, blank=False)
    creation_date = models.DateTimeField(verbose_name='creation date', auto_now_add=True, auto_now=False)
    upvotes = models.IntegerField(blank=True, default=0, null=True)

    class Meta:
        db_table = 'post'
        ordering = ['-creation_date']

    def __str__(self):
        return self.title


class Comment(models.Model):

    author = models.ForeignKey(Author, verbose_name='author', related_name='commentAuthor', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='content', max_length=1000)
    creation_date = models.DateTimeField(verbose_name='creation date', auto_now_add=True, auto_now=False)
    post = models.ForeignKey(Post, verbose_name='post', related_name='commentPost', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'
        ordering = ['-creation_date']
