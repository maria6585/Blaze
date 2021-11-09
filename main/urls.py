from os import name
from django.contrib import admin
from django.urls import path
from .views import delete, main, create, detail, update, delete
from django.conf.urls.static import static
from django.conf import settings

# from .views import PostCreate
# from .views import PostList, PostCreate, PostUpdate, PostDelete, PostDetail
# from .views import index

urlpatterns = [
    path('main/',main, name="main"),
    path('admin/', admin.site.urls),
    path('create/',create,name="create"),
    # path("", PostList.as_view(), name='main'),
    # path("create/", PostCreate.as_view(), name='create'),
    path('delete/<int:post_id>', delete, name="delete"),
    path('update/<int:post_id>',update, name="update"),
    path('detail/<int:post_id>', detail, name="detail"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


