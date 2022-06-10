from django.urls import path
from .views import home ,TodoDetail,delateTask

urlpatterns = [
  path('',home, name = 'home'),
  path('todo_app/<int:pk>',TodoDetail.as_view(),name = 'TodoDetail'),
  path('<int:id>/delate',delateTask, name = 'delateTask'),
] 
