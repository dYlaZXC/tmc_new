from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import BaseUpdateView

from apps.users.forms import UserModelForm


class CabinetIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'users/cabinet/index.html'


class CabinetUpdateUserInfo(LoginRequiredMixin, TemplateResponseMixin, BaseUpdateView):
    template_name = 'users/cabinet/update_user_info.html'
    form_class = UserModelForm
    success_url = reverse_lazy('users:cabinet:index')

    def get_object(self, queryset=None):
        return self.request.user
