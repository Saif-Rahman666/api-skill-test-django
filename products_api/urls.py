from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Creating a router instance and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
urlpatterns = router.urls