from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView

from apps.crm.models import ClientCall
from apps.surveys.forms import AnswerModelForm
from apps.surveys.models import Survey, Interview


class SurveyView(LoginRequiredMixin, DetailView):
    model = Survey
    template_name = 'surveys/survey.html'

    def post(self, *args, **kwargs):
        self.object = survey = self.get_object()
        answer_forms = self.get_answer_forms()
        if all([form.is_valid() for form in answer_forms]):
            client_call_pk = self.request.GET.get('call')
            client_call = ClientCall.objects.filter(pk=client_call_pk).first()
            client = client_call.client if client_call else None
            interview = Interview.objects.create(survey=survey, operator=self.request.user, client=client)
            for form in answer_forms:
                answer = form.save(commit=False)
                answer.interview = interview
                answer.save()
            messages.success(self.request, 'анкета сохранена')
            return redirect('index_page')
        else:
            return self.render_to_response(self.get_context_data(**kwargs))

    def get_answer_forms(self):
        if not hasattr(self, 'answer_forms'):
            self.answer_forms = list()
            for question in self.object.questions.all().order_by('text'):
                self.answer_forms.append(AnswerModelForm(self.request.POST or None,
                                                         prefix=question.id, initial={'question': question}))
        return self.answer_forms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_forms'] = self.get_answer_forms()
        return context
