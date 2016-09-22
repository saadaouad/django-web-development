from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If you want contact me, please send me an email']})

def experience(request):
	return render(request, 'personal/experience.html')

def formation(request):
	return render(request, 'personal/formation.html')

