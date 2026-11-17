from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import EmployeeViewSet, SkillViewSet, WorkplaceViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')
router.register('skills', SkillViewSet, basename='skill')
router.register('workplaces', WorkplaceViewSet, basename='workplace')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
