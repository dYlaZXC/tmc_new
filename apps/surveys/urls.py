from django.urls import path

from apps.surveys.views import SurveyView

app_name = 'surveys'

urlpatterns = [
    path('<int:pk>/', SurveyView.as_view(), name='survey'),
]
