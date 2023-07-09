from rest_framework_nested import routers

from store import views


router = routers.DefaultRouter()




router.register('customers', views.CustomerViewSet)
router.register('categories', views.VehicleCategoryViewSet)
router.register('vehicles', views.VehicleViewSet)


urlpatterns = router.urls