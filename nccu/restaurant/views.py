# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response,redirect
from restaurant.models import Restaurant,Comment,Photo
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .forms import RestaurantSearchForm
# Create your views here.
def home(request):
	return render(request,'restaurant/home.html')
'''
def weather(request):
	return render(request,'restaurant/weather.html')	
'''	
def restaurant(request, lat = "24.987579", lon = "121.576060"):
	restaurants = Restaurant.objects.all()
	lat = float(lat)
	lon = float(lon)
	return render_to_response('restaurant/restaurant.html',locals())

def add_restaurant(request):
	error = []
	if 'ok' in request.POST:
		name = request.POST['name']
		phone_number = request.POST['phone']
		address = request.POST['address']
		opentime  = request.POST['opentime']
	
		if not name:
			error.append('請輸入餐廳名稱')
		if not phone_number:
			error.append('請輸入電話')
		if not address:
			error.append('請輸入地址')
		if not opentime:
			error.append('請輸入營業時間')
		if not error:
			r = Restaurant(name = name,phone_number = phone_number,address = address,opentime = opentime)
			r.save()
			name = ''
			phone_number = ''
			address = ''
			opentime = ''
			return HttpResponseRedirect('/restaurant')
	return render_to_response('restaurant/add_restaurant.html',locals())

def comment(request,id):
	error = []
	if id:
		r = Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedirect('/restaurant')
	
	if 'ok' in request.POST:
		user = request.POST['user']
		content = request.POST['content']
		date_time = timezone.localtime(timezone.now())
		
		if not user:
			error.append('請輸入使用者')
		if not content:
			error.append('請評論')
		if not error:
			Comment.objects.create(
				user=user,
				content=content,
				date_time=date_time,
				restaurant=r
				)		
	return render_to_response('restaurant/comment.html',locals())
	
def bus(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurant/bus.html',locals())
		

def building(request):
	return render(request,'restaurant/building.html')

'''
No use --> see haystack.views.SearchView

def RestaurantSearch(request):
	form=RestaurantSearchForm(request.GET)
	restaurant=form.search()
	render_to_response("search/search.html",{"restaurant":restaurant})
'''
