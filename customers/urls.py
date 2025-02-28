from django.urls import path
from . import views
urlpatterns = [
    path('hello/',views.say_hello,name='say_hello'),
    path('posts/',views.post_list,name='post_list'),
    path('<int:post_id>/',views.One_Post,name='post_details'),
     path('create/',views.Create_post,name='post_create'),
     path('<int:post_id>/update/',views.Update_post,name='post_update'),
     path('<int:post_id>/delete/',views.delete_post,name='post_delete')
]
