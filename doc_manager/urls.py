from rest_framework.routers import SimpleRouter
from .views import DocumentViewSet

router = SimpleRouter()

router.register(r'document', DocumentViewSet)

urlpatterns = router.urls