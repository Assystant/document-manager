from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Document

class DocumentViewSetTestCase(APITestCase):
    def setUp(self):
        self.test_file = SimpleUploadedFile("file.txt", b"file_content")
        self.document = Document.objects.create(file=self.test_file)
    
    def test_upload(self):
        url = reverse('document-upload')
        data = {'file': self.test_file}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 2)

    def test_download(self):
        url = reverse('document-download', kwargs={'pk': self.document.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.content, b"file_content")
        
    def test_list(self):
        url = reverse('document-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.document.id)

    def test_retrieve(self):
        url = reverse('document-detail', kwargs={'pk': self.document.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.document.id)

    def test_delete(self):
        url = reverse('document-detail', kwargs={'pk': self.document.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Document.objects.count(), 0)
