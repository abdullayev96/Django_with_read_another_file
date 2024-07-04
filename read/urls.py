from django.urls import path
from .views import *






urlpatterns = [
    # path('move/', file_copy, name='file_move'),
    # path('status/', File_status, name='list_files'),
    path('count/', count_files_in, name='count_files'),

    path('add-folder/', add_folder, name='add_folder'),
    path('search/', search_files, name='search_files'),
    path('get/', get_files_in_folder, name='get_files_in_folder'),
]


