from django.urls import path
from . import views


app_name='blog'
urlpatterns=[
    path('BlogAdd',views.BlogAdd,name='BlogAdd'),
    path('',views.home,name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

]