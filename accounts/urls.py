from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from . import views


urlpatterns = [
     path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),

     #토큰
     # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     # path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
     #
]