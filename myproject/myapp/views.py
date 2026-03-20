from django.shortcuts import render, redirect, get_object_or_404

from .models import Member

# Create your views here.
def home(request):
    members = Member.objects.all()
    return render(request, 'home.html', {
        'members': members,
    })


def add_member(request):
    if request.method == 'POST':
        fname = request.POST.get('fname', '').strip()
        lname = request.POST.get('lname', '').strip()
        email = request.POST.get('email', '').strip()
        contact = request.POST.get('contact', '').strip()
        if fname and lname and email and contact:
            Member.objects.create(fname=fname, lname=lname, email=email, contact=contact)
        return redirect('home')
    return render(request, 'member_form.html', {'action': 'Add', 'member': None})


def update_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.fname = request.POST.get('fname', member.fname).strip()
        member.lname = request.POST.get('lname', member.lname).strip()
        member.email = request.POST.get('email', member.email).strip()
        member.contact = request.POST.get('contact', member.contact)
        member.save()
        return redirect('home')
    return render(request, 'member_form.html', {'action': 'Update', 'member': member})


def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('home')
    return render(request, 'member_confirm_delete.html', {'member': member})
