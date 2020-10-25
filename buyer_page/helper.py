from .models import *

def delete_transaction(transaction):
    transaction = Transactions.objects.filter(pk=transaction.pk)
    listing = transaction.listing
    listing = Listing.objects.filter(pk=listing.pk)
    listing.update_orders(orders=-transaction.quantity)
    models.Transactions.objects.filter(pk=transaction.pk).delete()

def get_all_product_categories():
    categories = Listing.objects.filter(active=True).order_by().values('category').distinct()

    return categories

def check_credentials(login_info):
	username = login_info["username"]
	password = login_info["password"]

	user = User.objects.filter(username=username, password=password)
	if len(user) < 1:
		return False

	return True