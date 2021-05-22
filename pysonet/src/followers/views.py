from rest_framework import generics, permissions, views, response
from .models import Follower
from .serializers import ListFollowerSerializer
from django.conf import settings

from ..profiles.models import UserNet


class ListFollowerView(generics.ListAPIView):
    """Вывод скписка подписчиков пользователя"""
    serializer_class = ListFollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class AddFollowerView(views.APIView):
    """Добавление в подписчики"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = UserNet.objects.filter(id=pk)
        if user.exists():
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=201)
        return response.Response(status=404)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)
