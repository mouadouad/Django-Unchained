
from django.urls import path
from . import views

urlpatterns=[
    path('render',views.render_upload, name='upload_render'),
    path('',views.upload, name='upload')
]