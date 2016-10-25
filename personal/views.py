from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If you want contact me, please send me an email']})

def experience(request):
	return render(request, 'personal/experience.html')

def formation(request):
	return render(request, 'personal/formation.html')

def hobbies(request):
	return render(request, 'personal/hobbies.html')

def error(request):
	return render(request, 'personal/404.html')

def thanks(request):
	return render(request, 'personal/thanks.html')
	
