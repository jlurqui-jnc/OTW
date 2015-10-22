from rest_framework import routers

from .views import OrdenView

router = routers.DefaultRouter()
router.register('ordenes', OrdenView)

urlpatterns = router.urls
