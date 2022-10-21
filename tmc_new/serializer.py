from typing import Tuple

from rest_framework import serializers

from .models import Appeal, User


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields: Tuple = (
            'id', 'date', 'fio', 'type_call', 'pmsp_name', 'user_fio', 'complaint_status', 'reason'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: Tuple = (
            '__all__'
        )
