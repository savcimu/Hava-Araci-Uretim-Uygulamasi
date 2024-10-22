from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from uretim import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="İHA Projesi API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'parcalar', views.ParcaViewSet)
router.register(r'ucaklar', views.UcakViewSet)
router.register(r'uretilen-ucaklar', views.UretilenUcakViewSet)
router.register(r'personeller', views.PersonelViewSet)
router.register(r'takimlar', views.TakimViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('personel-giris/', views.personel_giris, name='personel_giris'),
    path('personel-liste/', views.personel_liste, name='personel_liste'),
    path('parca/uret/', views.parca_uret, name='parca_uret'), 
    path('parca/sil/<int:parca_id>/', views.parca_sil, name='parca_sil'), 
    path('ucak-uret/', views.ucak_montaj, name='ucak_montaj'),
    path('uretilen-ucaklar/', views.uretilen_ucaklar_liste, name='uretilen_ucaklar_liste'),
    path('giris/', views.personel_giris, name='login'), 
    path('cikis/', views.personel_cikis, name='personel_cikis'),
    path('', views.index, name='index'), 
]
