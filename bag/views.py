from django.shortcuts import render, redirect, reverse


def bag_page(request):
    """A view to display the bag context page """

    return render(request, "bag/bag_page.html")


def add_to_bag(request, product_id):
    """ add a quantity for single product to the bag"""
    quantity = int(request.POST.get('quantity'))
    print(quantity)
    redirect_url = request.POST.get('redirect_url')
    print(redirect_url)
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag():
    """update bag to specified quantity of single product"""
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[id] = quantity
    else:
        bag.pop(id)

    request.session['bag'] = bag
    return redirect(reverse('bag_page'))
