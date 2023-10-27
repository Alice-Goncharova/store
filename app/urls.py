from rest_framework.routers import DefaultRouter

from app.views import UserModelViewSet, WarehouseModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('warehouse', WarehouseModelViewSet)
router.register('product', ProductModelViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)