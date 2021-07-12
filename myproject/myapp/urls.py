
from django.urls import path
from . import views
urlpatterns = [


    path('', views.index, name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('list/',views.list.as_view(),name='list'),
    path('detail/<int:pk>/', views.detail.as_view(), name='detail'),
    path('taskupdate/<int:pk>/', views.updatetask.as_view(), name='taskupdate'),
    path('taskdelete/<int:pk>/', views.deletetask.as_view(), name='delete'),

]