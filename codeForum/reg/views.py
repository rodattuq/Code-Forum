from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)



@csrf_exempt
def loginView(request):
	if request.method == 'POST':
		uname = request.POST['username']
		pword = request.POST['password']

		user = authenticate(username = uname,password = pword)
		if user is not None:
			login(request,user)
			return render_to_response('reg/login.html',{'logged_in': request.user.is_authenticated(),'user':uname})
		else:
			return HttpResponse("Inavlid user credntials!")

	form = LoginForm()
	return render_to_response('reg/login.html',{'form':form})


@csrf_exempt
def logoutView(request):
	logout(request)
	return render_to_response('reg/logout.html')





