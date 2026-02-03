from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import TeamMember, ProjectInfo, FutureUpdate, AppScreenshot, AppGallery, AppDownload

def home(request):
    app_screenshot = AppScreenshot.objects.filter(activa=True).first()
    app_gallery = AppGallery.objects.filter(activa=True).first()
    return render(request, 'stepmind/home.html', {
        'app_screenshot': app_screenshot,
        'app_gallery': app_gallery
    })

def about(request):
    project_info = ProjectInfo.objects.all()
    return render(request, 'stepmind/about.html', {'project_info': project_info})

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'stepmind/team.html', {'team_members': team_members})

def download(request):
    app_download = AppDownload.objects.filter(activa=True).first()
    return render(request, 'stepmind/download.html', {'app_download': app_download})

def download_apk(request, apk_id):
    apk = get_object_or_404(AppDownload, id=apk_id, activa=True)
    apk.incrementar_descargas()
    return HttpResponseRedirect(apk.archivo_apk.url)

def future(request):
    updates = FutureUpdate.objects.all().order_by('fecha_estimada')
    return render(request, 'stepmind/future.html', {'updates': updates})
