from django.conf.urls import include
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
from .views import ReservationListView

app_name = 'app_default'

urlpatterns = [
 
     #ex: /app_default/
     path('', views.IndexView.as_view(), name='index'),
     #ex: /app_default/5/
     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
     #ex: app_default/5/result/
     path('<int:pk>/results/',views.ResultView.as_view(), name='results'),
     #ex: /app_default/5/vote/
     path('<int:question_id>/vote/',views.vote, name='vote'),
     path('serializer/',ReservationListView.as_view(), name='serializer'),
]

schema_view = get_schema_view(
   openapi.Info(
        title="Test_Web API",
        default_version='v1',
        description="Test_WebPage",
        terms_of_service="http://www.googole.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   #본인은 해당 swagger ui를 사용할 것이다.
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ]