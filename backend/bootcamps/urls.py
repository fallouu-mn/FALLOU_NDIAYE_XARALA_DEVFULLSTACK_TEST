from django.urls import path
from .views import (
    BootcampList, BootcampDetail,
    LeadCreate, LeadList, LeadUpdate
)

urlpatterns = [
    path('bootcamps/', BootcampList.as_view(), name='bootcamp-list'),
    path('bootcamps/<int:pk>/', BootcampDetail.as_view(), name='bootcamp-detail'),
    path('leads/', LeadCreate.as_view(), name='lead-create'),
    path('admin/leads/', LeadList.as_view(), name='lead-list'),
    path('admin/leads/<int:pk>/', LeadUpdate.as_view(), name='lead-update'),
]
