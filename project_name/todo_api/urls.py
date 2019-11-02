from rest_framework import routers
from .views import TodoTask_ViewSet


router = routers.DefaultRouter()
router.register(r'todo', TodoTask_ViewSet)
urlpatterns = router.urls
