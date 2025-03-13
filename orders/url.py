from django.urls import path
from . import api_views
urlpatterns=[
    path('api/posts/',api_views.post_list,name='post_list'),
    path('api/posts/<int:post_id>/',api_views.detail_list,name='post_details'),
    path('api/create/',api_views.create_post,name='post_create'),
    path('api/update/<int:post_id>/',api_views.update_post,name='post_update'),
    path('api/delete/<int:post_id>/',api_views.delete_post,name='post_delete')
]