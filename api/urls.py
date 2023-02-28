from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet, TagsViewSet, PostsViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename = 'Users')
router.register('tags', TagsViewSet, basename = 'Tags')
router.register('posts', PostsViewSet, basename = 'Posts')

urlpatterns = [
    path('', include(router.urls)),
]
