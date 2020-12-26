from recipe import serializers
from core.models import Tag
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
form rest_framework.permissions import IsAuthenticated


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""
    authentication_classses = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
