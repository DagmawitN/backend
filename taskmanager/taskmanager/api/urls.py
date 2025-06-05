from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks_handler),               
    path('tasks/<int:id>/', views.task_detail),      
]
