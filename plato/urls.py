from rest_framework.routers import DefaultRouter
from .views import PlatoViewSet

api_router = DefaultRouter()

api_router.register('plato', PlatoViewSet, 'plato')

urlpatterns = api_router.urls
