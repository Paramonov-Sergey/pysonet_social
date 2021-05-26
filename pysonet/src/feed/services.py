from pysonet.src.profiles.models import UserNet
from pysonet.src.wall.models import Post
from rest_framework import views
from pysonet.src.followers.models import Follower


class Feed:
    '''service fieds'''

    def get_post_list(self, user):
        return Post.objects.filter(user__owner__subscriber=user).order_by('-create_date').select_related(
            'user').prefetch_related('comments')

    def get_single_post(self, pk: int):
        return Post.objects.select_related('user').prefetch_related('comments').get(id=pk)

feed_service = Feed()

# def feed(user):
#     # 1
#     news = []
#     subscribe = Follower.objects.filter(subscriber=user)
#     for sub in subscribe:
#         news.append(Post.objects.filter(user=sub.user, create_date__hour=1).order_by('-create_date'))
#
#     # 2
#     posts = Post.objects.filter(user__in=UserNet.objects.filter(owner__subscriber=user)).order_by('-create_date')
#
#     # 3
#     posts = Post.objects.filter(user__in=Follower.objects.values('user').filter(subscriber=user)).order_by(
#         '-create_date')
#
#     # 4
#     posts = Post.objects.filter(user__owner__subscriber=user).order_by('-create_date').select_related('user').prefetch_related('comments')
