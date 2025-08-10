from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render
from .models import Image
from .forms import UploadForm
from rembg import remove
# Create your views here.

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            original_img = form.cleaned_data["original_img"]
            imagebyte = original_img.read()
            edited  = remove(imagebyte, force_return_bytes=True)
            response = HttpResponse(edited, content_type="image/png")
            response['Content-Disposition'] = 'attachment; filename="no-bg.png"'
            
            return response



            # output = ContentFile(edited,  name='no-bg.png')
            # obj = Image()
            # obj.original_img= original_img
            # obj.new_img.save('no-bg.png', output)
            # obj.save()
            
    else:
        form = UploadForm()

    return render(request, "index.html", {'form':form})