from rest_framework.routers import SimpleRouter

from .views import LearningTopicViewset

router = SimpleRouter()
router.register('topic', LearningTopicViewset, basename='topic')

urlpatterns = [] + router.urls
