from django.http import FileResponse
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    @action(detail=False, methods=['POST'])
    def upload(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @action(detail=True)
    def download(self, request, pk=None):
        document = self.get_object()
        return FileResponse(document.file.open(), as_attachment=True, filename=document.file.name)
