from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index),
   path('users/',views.show, name="users"),  
   path('register/', views.register, name="register"),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('edit/<int:id>', views.edit, name="edit"),  
   path('update/<int:id>', views.update, name="update"),  
   path('delete/<int:id>', views.destroy, name="destroy"),
   path('profile/<int:id>', views.profile, name="user")
]