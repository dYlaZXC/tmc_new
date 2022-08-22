import xlwt
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, FormView, DetailView, UpdateView

from apps.common.xls_styles import BOLD_CELL_CENTER
from apps.crm.forms import ClientCallModelForm, ComplaintModelForm, ClientModelForm, ReportForm, \
    ConsultationModelForm, ComplaintUpdateModelForm
from apps.crm.models import ClientCall, Complaint
from apps.handbook.models import Category


class ClientCallDetailView(LoginRequiredMixin, DetailView):
    model = ClientCall
    template_name = 'crm/clientcall_detail.html'


# noinspection PyAttributeOutsideInit
class ClientCallFormView(LoginRequiredMixin, CreateView):
    template_name = 'crm/clientcall_form.html'
    form_class = ClientCallModelForm

    def get_client_form(self):
        if not hasattr(self, 'client_form'):
            self.client_form = ClientModelForm(self.request.POST or None,
                                               initial={'phone': self.kwargs.get('phone', '')})
        return self.client_form

    def get_complaint_form(self):
        if not hasattr(self, 'complaint_form'):
            self.complaint_form = ComplaintModelForm(self.request.POST or None)
        return self.complaint_form

    def get_consultation_form(self):
        if not hasattr(self, 'consultation_form'):
            self.consultation_form = ConsultationModelForm(self.request.POST or None)
        return self.consultation_form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_form'] = self.get_client_form()
        context['complaint_form'] = self.get_complaint_form()
        context['consultation_form'] = self.get_consultation_form()
        # данные для использования в javascript
        context['handbook_data'] = dict()
        for category in Category.objects.prefetch_related('article_set'):
            context['handbook_data'][category.id] = [{'id': article.id, 'name': article.name} for article in
                                                     category.article_set.order_by('name')]
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        self.client_form = self.get_client_form()
        self.complaint_form = self.get_complaint_form()
        self.consultation_form = self.get_consultation_form()
        if form.is_valid() and self.client_form.is_valid():
            if form.cleaned_data['kind'] == ClientCall.KINDS.complaint and not self.complaint_form.is_valid():
                return self.form_invalid(form)
            if form.cleaned_data['kind'] == ClientCall.KINDS.consultation and \
                    not self.consultation_form.is_valid():
                return self.form_invalid(form)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        client = self.client_form.save(commit=False)
        client.user = self.request.user
        client.save()
        self.object = clientcall = form.save(commit=False)
        clientcall.client = client
        clientcall.user = self.request.user
        clientcall.save()
        messages.success(self.request, 'обращение зарегистрировано')
        if clientcall.kind == ClientCall.KINDS.complaint:
            complaint = self.complaint_form.save(commit=False)
            complaint.operator = self.request.user
            complaint.save()
            self.complaint_form.save_m2m()
            clientcall.complaint = complaint
            clientcall.save()
            messages.success(self.request, 'жалоба создана')
        elif clientcall.kind == ClientCall.KINDS.consultation:
            consultation = self.consultation_form.save()
            clientcall.consultation = consultation
            clientcall.save()
            messages.success(self.request, 'консультация сохранена')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('index_page') #('surveys:survey', kwargs={'pk': 1}) + f'?call={self.object.pk}'


class ClientCallListView(LoginRequiredMixin, ListView):
    template_name = 'crm/clientcall_list.html'
    model = ClientCall
    paginate_by = 100
    queryset = ClientCall.objects.all().order_by('-id')
    # queryset = ClientCall.objects.select_related(
    #     'client', 'user', 'complaint', 'organization', 'region').prefetch_related(
    #     'complaint__topics').order_by('-created')


class ReportFormView(LoginRequiredMixin, FormView):
    template_name = 'crm/report_form.html'
    form_class = ReportForm
    success_url = reverse_lazy('crm:report_form')

    def form_valid(self, form):
        start = form.cleaned_data['start_date']
        end = form.cleaned_data['end_date']
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(f"отчёт по обращениям")
        headers = ["№ обращения",
                   "Дата и время поступления обращения",
                   "ФИО оператора / модератора",
                   "Регион",
                   "Наименование МО",
                   "ФИО заявителя",
                   "Конт.данные заявителя",
                   "Тематика обращения",
                   "Содержание обращения",
                   "Тип обращения",
                   "Статус обращения",
                   "Результат рассмотрения"]
        for i, header in enumerate(headers):
            ws.write(0, i, header, style=BOLD_CELL_CENTER)
        """
        for i, clientcall in enumerate(
                ClientCall.objects.filter(created__date__gte=start, created__date__lte=end).select_related(
                    'region', 'complaint', 'organization', 'client', 'user').prefetch_related(
                    'complaint__topics').order_by('created'), start=1):
            ws.write(i, 0, f'{clientcall.id}')
            ws.write(i, 1, timezone.localtime(clientcall.created).strftime('%d.%m.%Y %H:%M'))
            ws.write(i, 2, clientcall.user.get_full_name())
            ws.write(i, 3, str(clientcall.region) if clientcall.region else '')
            ws.write(i, 4, str(clientcall.organization) if clientcall.organization else '')
            ws.write(i, 5, clientcall.client.get_full_name() if clientcall.client else '')
            ws.write(i, 6, clientcall.client.phone if clientcall.client else '')
            topics = ', '.join(
                [str(topic) for topic in clientcall.complaint.topics.all()] if clientcall.complaint else '')
            ws.write(i, 7, topics)
            ws.write(i, 8, clientcall.text)
            ws.write(i, 9, clientcall.get_kind_display())
            ws.write(i, 10, clientcall.complaint.status if clientcall.complaint else '')
            ws.write(i, 11, clientcall.complaint.get_result_display() if clientcall.complaint else '')
        """
        for i, clientcall in enumerate(ClientCall.objects.filter(created__date__gte=start, created__date__lte=end), start=1):
            ws.write(i, 0, f'{clientcall.id}')
            ws.write(i, 1, timezone.localtime(clientcall.created).strftime('%d.%m.%Y %H:%M'))
            ws.write(i, 2, str(clientcall.fio_agent))
            ws.write(i, 3, str(clientcall.city) if clientcall.city else '')
            ws.write(i, 4, str(clientcall.pmsp) if clientcall.pmsp else '')
            ws.write(i, 5, clientcall.fio if clientcall.fio else '')
            ws.write(i, 6, clientcall.phone if clientcall.phone else '')
            topics = ', '.join(
                [str(topic) for topic in clientcall.complaint.topics.all()] if clientcall.complaint else '')
            ws.write(i, 7, topics)
            ws.write(i, 8, clientcall.reason)
            ws.write(i, 9, clientcall.kind)
            ws.write(i, 10, clientcall.result if clientcall.result else '')
            ws.write(i, 11, clientcall.result_more if clientcall.result_more else '')
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = f'attachment; filename="CRM {start: %d.%m.%Y}-{end: %d.%m.%Y}.xls"'
        wb.save(response)
        return response


class ComplaintListView(LoginRequiredMixin, ListView):
    model = Complaint
    template_name = 'crm/complaints/complaint_list.html'
    queryset = Complaint.objects.order_by('-created').prefetch_related('topics').select_related(
        'clientcall', 'clientcall__region', 'clientcall__client', 'clientcall__organization',
        'operator', 'assignor', 'executor')


class ComplaintUpdateView(LoginRequiredMixin, UpdateView):
    model = Complaint
    template_name = 'crm/complaints/complaint_form.html'
    form_class = ComplaintUpdateModelForm

    def form_valid(self, form):
        complaint = form.save(commit=False)
        complaint.executor = complaint.assignor = self.request.user
        complaint.save()
        messages.success(self.request, 'жалоба обновлена')
        return redirect('crm:complaint_list')
