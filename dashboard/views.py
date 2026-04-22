from django.shortcuts import render

def accueil(request):
    return render(request, 'dashboard/accueil.html')

def alertes(request):
    return render(request, 'dashboard/alertes.html')

def rapport_scan(request):
    return render(request, 'dashboard/rapport_scan.html')

def recommandations(request):
    return render(request, 'dashboard/recommandations.html')