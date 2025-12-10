from django.urls import path, include
from books.api.views import BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('crud', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls),),
]