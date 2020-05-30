from News_Board.celery import app
from .models import Post


@app.task
def clean_upvote():
    all_post = Post.objects.all()
    for post in all_post:
        post.upvotes = 0
        post.save()
