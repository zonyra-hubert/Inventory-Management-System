from django.urls import path
from . import views

urlpatterns=[
    path("home/", views.home_view, name="home"),
    path("", views.login_view, name="login"),
    path('create/', views.product_create_view, name="product_create"),
    path("list/", views.product_list_view, name="product_list"),
    path("update/<int:product_id>/", views.product_update_view, name="product_update"),
    path("delete/<int:product_id>/", views.product_delete_view, name="product_delete"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
]