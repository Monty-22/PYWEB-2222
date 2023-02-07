from django.shortcuts import render, get_object_or_404, redirect
from ..cart_shop.models import CartItemShop, Cart, Product
from apps.cart_shop.models import Product
from django.shortcuts import render
from django.views import View


class IndexShopView(View):
   def get(self, request):
       data = Product.objects.all()
       context = {'data': data}
       return render(request, 'home/index.html', context)

class AboutShopView(View):
   def get(self, request):
       return render(request, 'home/about.html')

class ContactShopView(View):
   def get(self, request):
       return render(request, 'home/contact.html')

# class ViewCartBuy(View):
#    def get(self, request, product_id):
#        product = get_object_or_404(Product, id=product_id)
#        cart_user = get_object_or_404(Cart, user=request.user)
#        cart_item = CartItemShop(cart=cart_user, product=product)
#        cart_item.save()
#        return  redirect('cart_shop:cart')
#
# class ViewCartAdd(View):
#    def get(self, request, product_id):
#        product = get_object_or_404(Product, id=product_id)
#        cart_user = get_object_or_404(Cart, user=request.user)
#        cart_item = CartItemShop(cart=cart_user, product=product)
#        cart_item.save()
#        return redirect('home:index')