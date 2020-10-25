import random

from django.shortcuts import render, redirect
from .models import *
from .helper import *
from .forms import *

def login(request):
	context = {}

	if request.method == "GET":
		login_form = LoginForm()
		context["form"] = login_form

		return render(request, "login.html", context)

	elif request.method == "POST":
		login_form = LoginForm(request.POST)

		if login_form.is_valid():
			login_info = login_form.cleaned_data
			valid_user = check_credentials(login_info=login_info)

			if valid_user:
				context["username"] = login_info["username"]
				return redirect(buyer_landing)

		context["form"] = login_form
		context["error"] = 1
		return render(request, "login.html", context)




# Create your views here.
def buyer_landing(request):
	context = {}

	if request.method == "GET":
		categories = get_all_product_categories()
		subset_categories = random.choices(categories, k=3)
		subset_categories = [category["category"] for category in subset_categories]
		urls = ["buyer_listing.html?category=" + category for category in subset_categories]
		image_paths = ["img/fruit.png", "img/shirt.jpg", "img/washing_machine.jpg"] 

		data = [{"category": subset_categories[i], "url": urls[i], "image_path": image_paths[i]} for i in range(len(urls))]

		context["data"] = data
		return render(request, "buyer_landing.html", context)

	else:
		return "In progress."




def buyer_listing(request, category):
	context = {}

	print(request)
	return render(request, "buyer_listing.html", context)
