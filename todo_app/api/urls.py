from django.urls import path
from todo_app.api.views import task_list,task_dateil

urlpatterns = [
  path('task/',task_list, name = 'task_list'),
  path('task/<int:id>',task_dateil, name = 'task_datail'),

] 
