from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.reviews_list, name="reviews_list"),
    path('create-review/', views.create_review, name='create_review'),
    path('some-view/', views.some_view, name='some_view_name'),
]
