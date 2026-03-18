from django.shortcuts import render

from .models import Member

# Create your views here.
def home(request):
    # Fetch all members so the template can render them in a table.
    members = Member.objects.all()

    return render(request, 'home.html', {
        'all': members,
    })
