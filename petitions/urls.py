from django.urls import path
from . import views

app_name = 'petitions'

urlpatterns = [
    path('', views.petition_list, name='petition_list'),
    path('<int:petition_id>/vote/', views.vote, name='vote'),
]