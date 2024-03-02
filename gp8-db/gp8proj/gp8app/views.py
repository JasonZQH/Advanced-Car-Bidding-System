# Create your views here.
from django.shortcuts import render
from .models import User


def testmysql(request):
    search_query = request.GET.get('search_query')  # Retrieve the search term from the GET request

    if search_query:
        users = User.objects.filter(userid__icontains=search_query)
    else:
        users = User.objects.all()

    if users:
        context = {
            'user_id': users[0].userid,
            'user_gender': users[0].gender,
            'user_age': users[0].age,
            'user_phone': users[0].phone,
            'user_email': users[0].email,

        }
    else:
        context = {
            'user_id': 'Not found',
            'user_gender': 'Not found',
            'user_age': 'Not found',
            'user_phone': 'Not found',
            'user_email': 'Not found',

        }
        
    return render(request, 'home.html', context)

