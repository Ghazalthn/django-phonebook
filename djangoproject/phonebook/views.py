from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

# Landing Page
@login_required
def landing_page(request):
    query = request.GET.get('search', '')
    if query:
        contacts = Contact.objects.filter(user=request.user, name__icontains=query)
    else:
        contacts = Contact.objects.filter(user=request.user)

    context = {
        'contacts': contacts,
        'search_query': query,
    }
    return render(request, 'phonebook/index.html', context)

# Create New Contact
@login_required
def create_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')

        # Validation
        if not name or not number:
            messages.error(request, "Name and number are required.")
            return redirect('landing-page')

        # Check if contact already exists for the user
        if Contact.objects.filter(user=request.user, name=name, number=number).exists():
            messages.error(request, "This contact already exists.")
            return redirect('landing-page')

        # Create the contact and associate it with the logged-in user
        Contact.objects.create(user=request.user, name=name, number=number)
        messages.success(request, "Contact added successfully.")
        return redirect('landing-page')

# Edit Contact
@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')

        if not name or not number:
            messages.error(request, "Name and number are required.")
            return redirect('edit-contact', contact_id=contact.id)

        contact.name = name
        contact.number = number
        contact.save()
        messages.success(request, "Contact updated successfully.")
        return redirect('landing-page')

    context = {'contact': contact}
    return render(request, 'phonebook/edit_contact.html', context)

# Delete Contact
@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    contact.delete()
    messages.success(request, "Contact deleted successfully.")
    return redirect('landing-page')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

class CustomLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, "You have successfully logged in.")
        return super().form_valid(form)