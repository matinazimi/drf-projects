from django.urls import path
from rest_framework import routers

from .views import PostView, ProfileView

router = routers.DefaultRouter()
# router.register(r'post', PostView,basename='postview')
router.register(r'profile', ProfileView)
#if use generic views you cant use routers
urlpatterns = [path('post/', PostView.as_view()), ]
urlpatterns += router.urls
