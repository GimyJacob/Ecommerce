from .models import Cart,CartItems
from .views import cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=cart_id(request))
            cat_items=CartItems.objects.all().filter(cart=cart[:1])
            for cat_item in cat_items:
                item_count += cat_item.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)