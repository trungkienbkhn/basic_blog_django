from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('new', views.create),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('<int:pk>/', views.post, name='post')
]