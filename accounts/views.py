from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Signup View
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect to 'next' if it exists, otherwise go to article_list
            return redirect(request.POST.get('next', 'article_list'))

    else:
        form = AuthenticationForm()  # Fixed missing parentheses

    return render(request, 'accounts/login.html', {'form': form})


# Logout View
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('article_list')
