from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewMember
from .models import Members
from .filters import MembersFilter


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, 'Login Successful')
            return redirect('home')
        else:
            # messages.success(request, 'Login Failed.. Try Again')
            return redirect('index')
    else:
        return render(request, 'main/index.html')


@login_required
def home(request):
    all_members = Members.objects.all()
    male_members = len(Members.objects.filter(Gender='M'))
    female_members = len(Members.objects.filter(Gender='F'))
    importers = len(Members.objects.filter(Operation_Mode='Importer'))
    retailers = len(Members.objects.filter(Operation_Mode='Retailer'))
    wholesalers = len(Members.objects.filter(Operation_Mode='Wholesaler'))
    ImportRtl = len(Members.objects.filter(Operation_Mode='ImportRtl'))
    paid_dues = len(Members.objects.filter(Dues_Payment='Paid'))

    return render(request, 'main/home.html', {
        'allmembers': len(all_members),
        'male_members': male_members,
        'female_members': female_members,
        'importers': importers,
        'retailers': retailers,
        'wholesalers': wholesalers,
        'ImportRtl': ImportRtl,
        'paid_dues': paid_dues,
    })


@login_required
def home1(request):
    all_members = Members.objects.all()

    my_filters = MembersFilter(request.GET, queryset=all_members)
    all_members = my_filters.qs

    context = {'all_members': all_members, 'my_filters': my_filters}
    # context = {'all_members': all_members}
    return render(request, 'main/home1.html', context)


@login_required
def members_preview(request):
    all_members = Members.objects.all()
    return render(request, 'main/members_preview.html', {'all_members': all_members})


@login_required
def register(request):
    if request.method == 'POST':
        form = NewMember(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Registration Successful')
            return redirect('home1')

    else:
        form = NewMember()

    context = {'form': form}
    return render(request, 'main/register.html', context)


@login_required
def view_details(request, member_id):
    try:
        view_detail = get_object_or_404(Members, pk=member_id)
        return render(request, 'main/view_details.html', {'view_detail': view_detail})
    except ValueError:
        return render(request, 'main/home1.html')
