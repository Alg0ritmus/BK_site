# upload multiple files ( just those with supported content_type) & store them to FileStorageSystem
# input: request from Form -> check UploadImg form
import os


from .forms import UploadImg
from django.core.files.storage import FileSystemStorage
# output: array with touples like this [(file.name,fileUrl)] 
# fileUrl -> based on FileStorageSystem
# file.name -> name of file, that is acctualy uploaded (it can differ from actual name in FileStorageSystem)
def uploadImg(request):
    
    uplaodForm = UploadImg(request.POST, request.FILES)
    if uplaodForm.is_valid():
        files = request.FILES.getlist('file_field')
        file_url = []
        for file in files:
            if file.content_type not in ['image/gifs','image/jpeg','image/png','image/svg+xml']:
                print("content/type error")
                return "Content/type error!"
            fs = FileSystemStorage()
            saved_file_name = fs.save(file.name, file)

            host = request.scheme+"://"+request.get_host()
            fileUrl=host+os.path.join(fs.base_url,saved_file_name)
            
            file_url.append((file.name, fileUrl))
        return file_url

    else:
        return uplaodForm.errors