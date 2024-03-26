from .models import Document
from rest_framework import serializers

class DocumentSerializer(serializers.ModelSerializer):
    file = serializers.FileField(max_length=200, allow_empty_file=True)
    class Meta:
        model = Document
        fields = '__all__'
