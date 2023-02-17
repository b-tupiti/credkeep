from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CredentialForm
from .models import Credential
from .utils import searchProjects

from django.http import JsonResponse

def home(request):
    return render(request, 'credentials/home.html')



@login_required(login_url="login")
def accounts(request):
    accounts, search_query = searchProjects(request)
    context = {'accounts': accounts, 'search_query':search_query }
    return render(request, 'credentials/accounts.html', context)


@login_required(login_url="login")
def account(request, pk):
    credential = Credential.objects.get(id=pk)
    context = {'account': credential }
    return render(request, 'credentials/account.html', context)

@login_required(login_url="login")
def createAccount(request):
    profile = request.user.profile
    form = CredentialForm()

    if request.method == 'POST':
        form = CredentialForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = profile
            account.save()
            messages.success(request,'Saved credentials for ' + account.credential_for)
            return redirect('accounts')

    context = {'form':form}
    return render(request, 'credentials/account_form.html', context)


@login_required(login_url="login")
def editAccount(request, pk):
    profile = request.user.profile
    account = profile.credential_set.get(id=pk)
    form = CredentialForm(instance=account)

    if request.method == 'POST':
        form = CredentialForm(request.POST, request.FILES, instance=account)
        if form.is_valid:
            form.save()
            messages.success(request,'Updated credentials for  ' + account.credential_for)
            return redirect('account', pk=account.id)

    context = {'form':form, 'account':account}
    return render(request, 'credentials/account_form.html', context)


@login_required(login_url="login")
def deleteAccount(request, pk):
    profile = request.user.profile
    account = profile.credential_set.get(id=pk)

    if request.method == 'POST':
        account.is_active = False
        account.save()
        messages.success(request,'You deleted credentials for ' + account.credential_for)
        return redirect('accounts')
    context = {'account':account}
    return render(request, 'credentials/delete_account.html', context)


