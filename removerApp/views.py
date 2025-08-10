from django.shortcuts import render
from .models import Image
from .forms import UploadForm
# Create your views here.

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadForm()

    return render(request, "index.html", {'form':form})