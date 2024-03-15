from blog import views
from django.urls import  path

app_name='blog'

urlpatterns = [
    path('', views.post_list, name='post_lists'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail')
]