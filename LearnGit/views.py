from django.shortcuts import render
def home(resquest):
	return render(resquest, 'pages/home.html')
