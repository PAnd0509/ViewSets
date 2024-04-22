from django.urls import path, include
from .views import ProjectAPIView,ProjectViewSet, TaskViewSet,CommentViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'projects',ProjectViewSet,basename='projects')
router.register(r'tasks',TaskViewSet,basename='Task')
router.register(r'comment',CommentViewSet,basename='comment')


"""urlpatterns=[
    path('projects/',ProjectAPIView.as_view()),
    path('tasks/',TaskAPIView.as_view()) 
    ]"""
urlpatterns=[
    
]

urlpatterns+=router.urls


    


