from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView

from apps.crm.models import ClientCall, Complaint


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientcall_count_all'] = ClientCall.objects.all().count()
        context['clientcall_count_month'] = ClientCall.objects.filter(
            created__month=timezone.now().month).count()
        context['complaint_count_all'] = Complaint.objects.count()
        context['complaint_count_month'] = Complaint.objects.filter(
            created__month=timezone.now().month).count()
        return context
