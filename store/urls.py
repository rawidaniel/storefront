from django.urls import path, include
from . import views



urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetails.as_view()),
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail')
]