import json

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import contactdata, gallery, blogmod, Shopproduct, order, orderiteminfo


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def galleryfunc(request):
    gal = gallery.objects.all()

    return render(request, 'gallery.html', {'gal': gal})


def gallerysinglepost(request, id2):
    ggg = gallery.objects.get(id=id2)
    return render(request, 'gallery-single-post.html', {'ggg': ggg})


def blog(request):
    blog = blogmod.objects.all()

    return render(request, 'blog.html', {'blog_d': blog})


def blogsinglepost(request, id):
    bbb = blogmod.objects.get(id=id)
    return render(request, 'blog-single-post.html', {'bbb': bbb})


def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact_d = contactdata(fname=fname, address=address, email=email, phone=phone, message=message)
        contact_d.save()
        return redirect('contact')
    else:
        return render(request, 'contact.html')


def shop(request):
    product = Shopproduct.objects.all()
    return render(request, 'shop.html', {'product': product})


def shopsingleproduct(request, id3):
    product = Shopproduct.objects.get(id=id3)
    return render(request, 'shop-single-product.html', {'product': product})


def checkout(request):
    if request.method == "POST":
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        phone = request.POST.get('cphone')
        address = request.POST.get('caddress')
        city = request.POST.get('ccity')
        state = request.POST.get('cstate')
        zip_code = request.POST.get('czip')
        items_json = request.POST.get('itemsJson')
        order_payment_type = request.POST.get('orderpaymenttype')
        order_payment_status = request.POST.get('orderpaymentstatus')
        order_status = request.POST.get('orderstatus')
        item_num = request.POST.get('itemnum')
        finaltotal = request.POST.get('finaltotal')

        thank = True
        item_info = json.loads(items_json)

        print(name, email, address, city, state, zip_code, phone, order_payment_type, order_payment_status,
              order_status, item_num, finaltotal)
        order2 = order(cust_name=name, cust_email=email, cust_phone=phone, cust_address=address, cust_city=city,
                       cust_state=state, cust_zip_code=zip_code, order_payment_type=order_payment_type,
                       order_payment_status=order_payment_status, order_status=order_status, order_item_num=item_num,
                       order_grand_total=finaltotal)

        order2.save()

        for item_info_db in item_info:
            order_prod_id = item_info_db
            order_prod_qty = item_info[item_info_db][0]
            order_prod_name = item_info[item_info_db][1]
            order_prod_price = item_info[item_info_db][2]
            order_prod_totalprice = item_info[item_info_db][3]
            print(order_prod_id, order_prod_qty, order_prod_name, order_prod_price, order_prod_totalprice)
            orderitem2 = orderiteminfo(order_id=order2.id, product_id=order_prod_id, order_item_name=order_prod_name,
                                       order_item_qty=order_prod_qty, order_item_price=order_prod_price,
                                       order_item_total_price=order_prod_totalprice)
            orderitem2.save()

        return render(request, 'checkout.html', {'thank': thank, 'id': order2.id})

    return render(request, 'checkout.html')


def trackorder(request):
    if request.method == 'POST':
        orderid = request.POST['orderid']
        email = request.POST['email']

        try:
            oo = order.objects.get(id=orderid, cust_email=email)
            oooi = orderiteminfo.objects.filter(order_id=orderid)

            return render(request, 'trackorder.html', {'oo': oo, 'oooi': oooi})
        except:
            error = 'not found'
            return render(request,'trackorder.html',{'error':error})

    return render(request, 'trackorder.html')
