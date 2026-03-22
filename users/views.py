from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.forms import RegisterForm

# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            # username=form.cleaned_data.get("username")
            # password=form.cleaned_data.get("password1")
            # confirm_password=form.cleaned_data.get("password2")

            # if password==confirm_password:
            #     User.objects.create(username=username, password=password)
            # else:
            #     print("passwords do not match")
            form.save()
        else:
            print("form is not valid")

    # context = {'form': form}

    
    return render(request, 'registration/registration.html', {'form':form})
