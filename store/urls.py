from rest_framework_nested import routers

from store import views


router = routers.DefaultRouter()




router.register('customers', views.CustomerViewSet)
router.register('mechanics', views.MechanicViewSet)
router.register('categories', views.VehicleCategoryViewSet)
router.register('vehicles', views.VehicleViewSet)
router.register('repair_requests', views.VehicleRepairRequestViewSet)

vehicle_router = routers.NestedDefaultRouter(router, 'vehicles', lookup='vehicle')
vehicle_router.register('parts', views.VehiclePartViewSet , basename='vehicle-parts')


mechanic_router = routers.NestedDefaultRouter(router, 'mechanics', lookup='mechanic')
mechanic_router.register('reviews', views.ReviewViewSet , basename='mechanic-reviews')


repair_request_router = routers.NestedDefaultRouter(router, 'repair_requests', lookup='repair_request')
repair_request_router.register('images', views.VehicleRepairRequestImageViewSet , basename='repair_request-images')



urlpatterns = router.urls + vehicle_router.urls + mechanic_router.urls + repair_request_router.urls