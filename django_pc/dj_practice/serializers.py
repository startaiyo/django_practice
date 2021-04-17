from rest_framework import serializers
from .models import Memo

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'skill_name',
            'content',
            'status'
        )
        model = Memo