from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Petition

@login_required
def petition_list(request):
    # Handle the creation of a new petition
    if request.method == 'POST':
        title = request.POST.get('title')
        reason = request.POST.get('reason')
        if title and reason:
            Petition.objects.create(title=title, reason=reason, author=request.user)
            return redirect('petitions:petition_list')

    petitions = Petition.objects.all().order_by('-created_at')

    # Get a list of petitions the current user has already voted on
    voted_petition_ids = list(request.user.voted_petitions.values_list('id', flat=True))

    template_data = {
        'title': 'Petitions',
        'petitions': petitions,
        'voted_petition_ids': voted_petition_ids,
    }
    return render(request, 'petitions/petition_list.html', {'template_data': template_data})

@login_required
def vote(request, petition_id):
    if request.method == 'POST':
        petition = get_object_or_404(Petition, id=petition_id)
        user = request.user

        # If user is in the list of votes, remove them. Otherwise, add them.
        if petition.votes.filter(id=user.id).exists():
            petition.votes.remove(user)
        else:
            petition.votes.add(user)
    return redirect('petitions:petition_list')