from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .controllers import DogViewSet, BreedViewSet


router = DefaultRouter()

router.register(r'dogs', DogViewSet)
router.register(r'breeds', BreedViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
