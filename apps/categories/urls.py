from rest_framework.routers import DefaultRouter

from apps.categories.views import CategoryApiView

router = DefaultRouter()
router.register('', CategoryApiView, "api_category")

urlpatterns = router.urls