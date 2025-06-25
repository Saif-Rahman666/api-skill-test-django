from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Creating a router instance and register our viewsets with it.
router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')
# The API URLs are now determined automatically by the router.
urlpatterns = router.urls