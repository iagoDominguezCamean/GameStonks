from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/<store_id>/', views.store, name='store'),
    path('deals/<path:deal_id>/', views.deal, name='deal'),
    path('sBn/', views.sBn, name='sBn'),
    path('analisis/', views.analisis, name='analisis'),
    path('register/', views.register, name='register'),
    path('login/', views.login_req, name='login'),
    path('logout/', views.logout_req, name='logout'),
    path('account/', views.account, name='account')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
