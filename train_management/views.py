from django.shortcuts import render


def dashboard(request):
    return render(request, "train_management/dashboard.html")
