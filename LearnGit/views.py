from django.shortcuts import render
def home(resquest):
	return render(resquest, 'pages/home.html')
def about(resquest):
	return render(resquest, 'pages/about.html')
def contact(resquest):
	return render(resquest, 'pages/contact.html')
