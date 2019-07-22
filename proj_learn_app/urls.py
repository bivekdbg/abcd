from rest_framework import routers
from .views import DreamRealViewSet

router = routers.SimpleRouter()
router.register(r'DreamReal', DreamRealViewSet)  # here r==>regular expression
urlpatterns = router.urls
