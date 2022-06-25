from django.urls import path

from photos import views
app_name="photos"
urlpatterns = [
    path("", views.galleries_list, name="gallery_list")
]