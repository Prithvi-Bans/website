from  django.urls import path
from . import views

urlpatterns = [
	path('', views.PostListView.as_view(), name="postview"),
	path('create/', views.PostCreateView.as_view(), name="postcreate"),
	path('users/', views.PostUserView.as_view(), name="postuser"),
	path('edit/<int:pk>', views.PostUpdateView.as_view(), name="postupdate"),
	path('delete/<int:pk>', views.PostDeleteView.as_view(), name="postdelete"),
	path('likes/<int:pk>', views.PostLikeView, name="postlike"),
]