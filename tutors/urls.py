from django.urls import path
from .views import Home, FilterBySubject, BulkUpload, DownloadTutors, DownloadBySubject

urlpatterns = [
    path('', Home, name='home'),
    path('getTutors/<str:subject>/', FilterBySubject, name='bySubject'),
    path('bulkUpload/', BulkUpload, name='bulkUpload'),
    path('downloads/allTutors', DownloadTutors, name='download-allTutors'),
    path('download/<str:subject>', DownloadBySubject, name='download-bysubject')
]
