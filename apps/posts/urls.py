from rest_framework.routers import DefaultRouter

from apps.posts.views import PostApiView

router = DefaultRouter()
router.register('', PostApiView, "api_posts")

urlpatterns = router.urls