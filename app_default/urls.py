from django.urls import path
from . import views


app_name = 'app_default'

urlpatterns = [
     #ex: /app_default/
     path('', views.index, name='index'),
     #ex: /app_default/5/
     path('<int:question_id>/', views.detail, name='detail'),
     #ex: app_default/5/result/
     path('<int:question_id>/results/',views.results, name='results'),
     #ex: /app_default/5/vote/
     path('<int:question_id>/vote/',views.vote, name='vote')
]