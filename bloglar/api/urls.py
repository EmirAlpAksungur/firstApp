from django.urls import path
from bloglar.api import views as api_views

urlpatterns = [
   path('bloglar/',api_views.BlogListCreateAPIView.as_view(), name='blog-listesi' ),
   path('bloglar/<int:pk>', api_views.BlogDetailAPIView.as_view(), name='blog-bilgileri'),
]