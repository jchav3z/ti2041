from django.urls import path
from .views import ServiceList, ServiceDetail, ProviderDetail, service_list

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
    path('providers/<int:pk>/', ProviderDetail.as_view(), name='provider-detail'),
    path('services-html/', service_list, name='service-list-html'),
]
