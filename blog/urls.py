from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('projects', views.ProjectViewset) # router er antena
router.register('post', views.BlogPostViewset) # router er antena

urlpatterns = [
    path('', include(router.urls)),
    path('project/<int:project_id>/donate/', views.DonationsView.as_view(), name='donate'),
]