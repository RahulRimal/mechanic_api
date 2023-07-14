from rest_framework_nested import routers

from store import views


router = routers.DefaultRouter()




router.register('customers', views.CustomerViewSet)
router.register('categories', views.VehicleCategoryViewSet)
router.register('vehicles', views.VehicleViewSet)
# router.register('vehicles', views.VehicleViewSet)

vehicle_router = routers.NestedDefaultRouter(router, 'vehicles', lookup='vehicle')
vehicle_router.register('parts', views.VehiclePartViewSet , basename='vehicle-parts')


urlpatterns = router.urls + vehicle_router.urls