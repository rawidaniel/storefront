from django.shortcuts import render
from django.http  import HttpResponse
from django.db.models import Q,F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Max, Min, Avg, Count, Sum
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem
import json

# Create your vie3ws here.

def say_hello(request):
    # query_set = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))
    # query_set = Product.objects.filter(id=F('orderitem__product_id')).order_by('title')
    # query_set = Product.objects.filter(id__in= OrderItem.objects.values('product_id').distinct())
    # query_set = OrderItem.objects.select_related('product__collection').all()
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'))
    # print(result)
    # query_set = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    # query_set = Customer.objects.annotate(full_name= Concat('first_name', Value(' '), 'last_name'))
    # query_set = Customer.objects.annotate(order_count=Count('order')).filter(order_count=5, membership  ='G')
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # query_set = Product.objects.annotate(discounted_price=discounted_price)
    # content_type = ContentType.objects.get_for_model(Product)
    # query_set = TaggedItem.objects.select_related('tag').filter(content_type=content_type, object_id=1)
    # query_set = TaggedItem.objects.get_tags_for(Product, 1)
    # list(query_set)
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()


    #     orderItem = OrderItem()
    #     orderItem.order = order
    #     orderItem.product = 1
    #     orderItem.quantity = 3
    #     orderItem.unit_price = 3000
    #     orderItem.save()

    # cursor= connection.cursor()
    # cursor.execute("SELECT * FROM store_product")
    # query_set = cursor.fetchall()
    # cursor.close()

    query_set = Product.objects.raw("SELECT id, title FROM store_product")

    for product in query_set:
        print(product.title)
    # return HttpResponse("Hello World")
    return render(request, 'hello.html')