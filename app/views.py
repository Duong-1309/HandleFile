from django.shortcuts import render, get_object_or_404
from .models import FileUpload
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="admin/")
def Home(request):
    context = {"files": FileUpload.objects.all()}
    return render(request, 'home.html', context)

@login_required(login_url="admin/")
def Handle(request, pk):
    handleFile = get_object_or_404(FileUpload, pk=pk)
    context = {"file": handleFile}
    return render(request, "handle.html", context)