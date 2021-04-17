from django.urls import path
from . import views
urlpatterns = [
    path('', views.memo_list),
    path('<int:pk>/', views.memo_detail),
]