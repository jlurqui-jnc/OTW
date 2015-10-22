from rest_framework import routers

from .views import AccionView, MaterialView, OrdenView

router = routers.DefaultRouter()
router.register('ordenes', OrdenView)
router.register('acciones', AccionView)
router.register('material', MaterialView)


urlpatterns = router.urls
