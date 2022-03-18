from django.shortcuts import render
from cricapp.models import Cricketer

# Create your views here.
def home_page(request):
	return render(request = request, template_name = 'cricapp/homepage.html')

def display_data(request):
	cric_data = Cricketer.objects.all()
	print(cric_data)
	print(type(cric_data))

	my_dict = {'cric_data':cric_data} 

	return render(request = request, template_name ='cricapp/display.html',context = my_dict)