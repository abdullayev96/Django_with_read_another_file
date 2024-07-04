from django.shortcuts import render
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
import shutil
from .forms import *
from .utils import *
from django.http import JsonResponse


#
# # def handle_uploaded_file(file, destination_path):
# #     with open(destination_path, 'wb+') as destination:
# #         for chunk in file.chunks():
# #             destination.write(chunk)
# #
# #
#
# #
# # def file_upload_view(request):
# #     if request.method == 'POST':
# #         form = FileUploadForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             uploaded_file = form.cleaned_data['file']
# #             # Define the destination path
# #             destination_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
# #             # Save the uploaded file to the destination
# #             handle_uploaded_file(uploaded_file, destination_path)
# #             return HttpResponse(f"File uploaded to: {destination_path}")
# #     else:
# #         form = FileUploadForm()
# #     return render(request, 'upload.html', {'form': form})
# #
#
# #
# # def handle_uploaded_file(file, destination_path):
# #     with open(destination_path, 'wb+') as destination:
# #         for chunk in file.chunks():
# #             destination.write(chunk)
# #
# #
# #
# #
# # def file_upload_view(request):
# #     if request.method == 'POST':
# #         form = FileUploadForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             uploaded_file = form.cleaned_data['file']
# #             destination_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
# #             handle_uploaded_file(uploaded_file, destination_path)
# #
# #             # Save to model
# #             my_model_instance = MyModel(file=uploaded_file)
# #             my_model_instance.save()
# #
# #             return HttpResponse(f"File uploaded to: {destination_path}")
# #     else:
# #         form = FileUploadForm()
# #     return render(request, 'upload.html', {'form': form})
#
#
#
#
# def file_move(request):
#     try:
#         file_choices = [(f, f) for f in os.listdir(settings.MEDIA_ROOT) if os.path.isfile(os.path.join(settings.MEDIA_ROOT, f))]
#     except FileNotFoundError:
#         file_choices = []
#
#     if request.method == 'POST':
#         form = FileMoveForm(request.POST, file_choices=file_choices)
#         if form.is_valid():
#             selected_file = form.cleaned_data['file']
#             destination_path = form.cleaned_data['destination']
#
#             destination_full_path = os.path.join(settings.MEDIA_ROOT, destination_path)
#             os.makedirs(os.path.dirname(destination_full_path), exist_ok=True)
#
#             shutil.move(
#                 os.path.join(settings.MEDIA_ROOT, selected_file),
#                 destination_full_path
#             )
#
#             return HttpResponse(f"File moved to: {destination_full_path}")
#     else:
#         form = FileMoveForm(file_choices=file_choices)
#
#     return render(request, 'move_file.html', {'form': form})


# def file_copy(request):
#     primary_directory = settings.MEDIA_ROOT
#     secondary_directory = os.path.join(settings.MEDIA_ROOT, 'secondary')
#
#
#     try:
#         file_choices = [(f, f) for f in os.listdir(primary_directory)
#                         if os.path.isfile(os.path.join(primary_directory, f))]
#     except FileNotFoundError:
#         file_choices = []
#
#     if request.method == 'POST':
#         form = FileMoveForm(request.POST, file_choices=file_choices)
#         if form.is_valid():
#             selected_file = form.cleaned_data['file']
#             destination_path = form.cleaned_data['destination']
#
#             # Ensure the destination directory exists
#             destination_full_path = os.path.join(secondary_directory, destination_path)
#             os.makedirs(os.path.dirname(destination_full_path), exist_ok=True)
#
#             # Copy the file
#             shutil.copy2(
#                 os.path.join(primary_directory, selected_file),
#                 destination_full_path
#             )
#
#             #return HttpResponse(f"File copied to: {destination_full_path}")
#             return redirect('file_move')
#     else:
#         form = FileMoveForm(file_choices=file_choices)
#
#     return render(request, 'move_file.html', {'form': form})
#


#
# def List_files(request):
#     primary_directory = settings.MEDIA_ROOT
#     files_info = []
#
#     try:
#         for file_name in os.listdir(primary_directory):
#             if os.path.isfile(os.path.join(primary_directory, file_name)):
#                 file_path = os.path.join(primary_directory, file_name)
#
#                 verified_status = 'True' if is_verified(file_name) else 'False'
#                 files_info.append({
#                     'name': file_name,
#                     'status': verified_status,
#                 })
#     except FileNotFoundError:
#         files_info = []
#
#
#     return render(request, 'list.html', {'files_info': files_info})


# def File_status(request):
#     primary_directory = settings.MEDIA_ROOT
#     files_info = []
#     counts = count_files(primary_directory)
#
#     try:
#         for file_name in os.listdir(primary_directory):
#             if os.path.isfile(os.path.join(primary_directory, file_name)):
#                 approval_status = 'True' if is_verified(file_name) else 'False'
#                 files_info.append({
#                     'name': file_name,
#                     'status': approval_status,
#                 })
#     except FileNotFoundError:
#         files_info = []
#
#     context = {
#         'files_info': files_info,
#         'approved_count': counts['approved'],
#         'not_approved_count': counts['not_approved'],
#     }
#
#     return render(request, 'list.html', context)
#


#
# def count_files_in_folder(request):
#     if request.method == 'POST':
#         folder_path = request.POST.get('folder')
#
#         if not os.path.exists(folder_path):
#             return HttpResponse(f"Directory does not exist: {folder_path}")
#
#
#         num_files = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
#
#         return HttpResponse(f"The folder contains {num_files} files.")
#
#     return render(request, 'uploads.html')


# def count_files_in(request):
#     if request.method == 'POST':
#         folder_path = request.POST.get('folder')
#
#         if not os.path.exists(folder_path):
#             return HttpResponse(f"Directory does not exist: {folder_path}")
#
#
#         num_files = sum([len(files) for _, _, files in os.walk(folder_path)])
#
#         return HttpResponse(f"The folder and its subdirectories contain {num_files} files.")
#
#     return render(request, 'uploads.html')



def count_files_in(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder_path = form.cleaned_data['folder'].strip()

            if not os.path.exists(folder_path):
                return HttpResponse(f"Directory does not exist: {folder_path}", status=404)

            num_files = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])

            return HttpResponse(f"The folder contains {num_files} files.")
    else:
        form = FolderForm()

    return render(request, 'uploads.html', {'form': form})




def add_folder(request):
    if request.method == 'POST':
        form = FoldersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search_files')
    else:
        form = FolderForm()
    return render(request, 'add_folder.html', {'form': form})



def list_folders(request):
    folders = DataFile.objects.all()
    folder_contents = {folder.path: os.listdir(folder.path) for folder in folders if os.path.exists(folder.path)}
    return render(request, 'list_folders.html', {'folders': folder_contents})

#
# def search_files(request):
#     search_results = []
#     if request.method == 'POST':
#         form = FolderSearchForm(request.POST)
#         if form.is_valid():
#             folder_path = form.cleaned_data['folder_path'].strip()
#             file_name = form.cleaned_data['file_name'].strip()
#
#             if os.path.exists(folder_path):
#                 # Search for files that match the query
#                 search_results = [f for f in os.listdir(folder_path) if file_name.lower() in f.lower()]
#             else:
#                 return HttpResponse(f"Directory does not exist: {folder_path}", status=404)
#
#     else:
#         form = FolderSearchForm()
#
#     return render(request, 'search_files.html', {'form': form, 'search_results': search_results})



def search_files(request):
    search_results = []
    selected_files = []
    form = FolderSelectForm()

    if request.method == 'POST':
        form = FolderSelectForm(request.POST)
        if form.is_valid():
            folder = form.cleaned_data['folder']
            file_name = form.cleaned_data['file_name'].strip()

            if os.path.exists(folder.path):

                all_files = os.listdir(folder.path)
                selected_files = [f for f in all_files if os.path.isfile(os.path.join(folder.path, f))]

                if file_name:

                    search_results = [f for f in selected_files if file_name.lower() in f.lower()]

    return render(request, 'search_files.html', {
        'form': form,
        'selected_files': selected_files,
        'search_results': search_results
    })




def get_files_in_folder(request):
    folder_path = request.GET.get('folder', '').strip()
    files = []
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return JsonResponse({'files': files})