from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! now login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})
