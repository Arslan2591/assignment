# urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ApartmentViewSet, ResidentViewSet, PostListView, PostDetailView,ResidentByApartment

router = DefaultRouter()
router.register(r'apartments', ApartmentViewSet)
router.register(r'residents', ResidentViewSet)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
     path('apartments/<int:apartment_id>/residents/', ResidentByApartment.as_view()),
]

urlpatterns += router.urls

# /posts/?resident=<resident_id>
# /posts/?apartment=<apartment_id>

