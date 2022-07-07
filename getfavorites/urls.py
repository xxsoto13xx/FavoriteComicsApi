from rest_framework import routers
from .api.views import GetComicsApiViewSet

router = routers.SimpleRouter()
router.register('', GetComicsApiViewSet, basename='getfavorites')
urlpatterns = router.urls
