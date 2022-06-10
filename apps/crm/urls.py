from django.urls import path

from apps.crm.views import ClientCallFormView, ClientCallListView, ReportFormView, ClientCallDetailView, \
    ComplaintListView, ComplaintUpdateView

app_name = 'crm'

urlpatterns = (
    path('calls/', ClientCallListView.as_view(), name='clientcall_list'),
    path('calls/<int:pk>/', ClientCallDetailView.as_view(), name='clientcall_detail'),
    path('call-form/', ClientCallFormView.as_view(), name='new_clientcall_form'),
    path('call-form/<slug:phone>/', ClientCallFormView.as_view(), name='clientcall_form'),
    path('reports/create/', ReportFormView.as_view(), name='report_form'),
    path('complaints/', ComplaintListView.as_view(), name='complaint_list'),
    path('complaints/<int:pk>/update/', ComplaintUpdateView.as_view(), name='complaint_update'),
)
