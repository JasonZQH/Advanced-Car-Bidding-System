from django.shortcuts import render
from .models import User


def testmysql(request):
    user = User.objects.all()


    context = {
    'user_id': user[0].userid,
    'user_gender': user[3].gender,
    }
    return render(request, 'home.html', context)


# Create your views here.
