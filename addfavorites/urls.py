from rest_framework import routers
from addfavorites.api.views import AddComicsApiViewSet

router = routers.SimpleRouter()
router.register('', AddComicsApiViewSet, basename='addfavorites')
urlpatterns = router.urls
