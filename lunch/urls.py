from django.urls import include, path
from rest_framework import routers
from lunch import views

router = routers.DefaultRouter()
router.register(r'plans', views.PlanViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)), 
    path("next/", views.NextWeekPlan.as_view(), name="next_week"), 
    path('switch/<int:pk>/', views.SwitchPlan.as_view(), name="switch_plan"), 
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]