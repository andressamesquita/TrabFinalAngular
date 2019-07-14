"""embrapaBee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from bee import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


router = routers.DefaultRouter()
router.register('apicultores', views.ApicultorViewSet, base_name='apicultores')
router.register('apiarios', views.ApiarioViewSet, base_name='apiarios')
router.register('caixas_racionais', views.CaixaRacionalViewSet, base_name='caixas_racionais')
router.register('perdas', views.PerdaViewSet, base_name='perdas')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
]
