from django.shortcuts import render


def frontpage(request):
    print(request.user)
    return render(request, 'frontpage.html')
