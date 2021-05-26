from rest_framework import generics, viewsets, permissions, response

from ..wall.models import Post

from ..wall.serializers import ListPostSerializer, PostSerializer


class FeedView(viewsets.ReadOnlyModelViewSet):
    """View follower's feed"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class_by_action = {'list': ListPostSerializer, 'retrieve': PostSerializer}

    def get_queryset(self):
        if self.action == 'list':
            return Post.objects.filter(user__owner__subscriber=self.request.user).order_by(
                '-create_date').select_related(
                'user').prefetch_related('comments')
        elif self.action == 'retrieve':
            return Post.objects.select_related('user').prefetch_related('comments')

    def get_serializer_class(self):
        return self.serializer_class_by_action[self.action]
        # if self.action == 'list':
        #     return ListPostSerializer
        #
        # elif self.action == 'retrieve':
        #     return PostSerializer

    # Второй вариант
    # def list(self, request, *args, **kwargs):
    #     queryset = feed_service.get_post_list(request.user)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return response.Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = feed_service.get_single_post(kwargs.get('pk'))
    #     serializer = PostSerializer(instance)
    #     return response.Response(serializer.data)
