# Create your views here.
from django.shortcuts import render
from .models import User


def testmysql(request):
    user = User.objects.all()


    context = {
    'user_id': user[0].userid,
    'user_gender': user[0].gender,
    }
    return render(request, 'home.html', context)



