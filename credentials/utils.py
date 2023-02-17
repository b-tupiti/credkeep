
def searchProjects(request):

    profile = request.user.profile
    accounts = profile.credential_set.all()

    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        accounts = accounts.filter(credential_for__icontains=search_query, is_active=True)

    accounts = accounts.filter(credential_for__icontains=search_query,  is_active=True)

    return accounts, search_query


