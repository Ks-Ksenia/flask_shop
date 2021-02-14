from random import randint

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

from app import db
from models import *
from forms import OrderForm


cart = Blueprint('basket', __name__, template_folder='templates/cart')

@cart.route('/')
@login_required
def get_cart():
    if not current_user.customer:
        customer = Customer(user=current_user)
        cart = Cart(customer=customer, total_products=0, final_price=0)

        db.session.add(cart)
        db.session.commit()
    else:
        customer = Customer.query.filter(Customer.user == current_user).first()
        cart = Cart.query.filter(Cart.customer == customer).first()

    return render_template('cart.html', cart=cart)


@cart.route('/add_product/<path:url>')
@login_required
def add_product(url):
    if not current_user.customer:
        customer = Customer(user=current_user)
        cart = Cart(customer=customer, total_products=0, final_price=0)

        db.session.add(cart)
        db.session.commit()

    else:
        customer = Customer.query.filter(Customer.user == current_user).first()
        cart = Cart.query.filter(Cart.customer == customer).first()

    product = Product.query.filter(Product.url == url).first()
    cart_product = CartProduct.query.filter(CartProduct.cart.contains(cart),
                                            CartProduct.product == product.id).first()

    if not cart_product:
        cart_product = CartProduct(cart=[cart],
                                   product=product.id,
                                   product_price=product.price,
                                   final_price=product.price)

        db.session.add(cart_product)
        db.session.commit()

    return redirect(url_for('.get_cart'))


@cart.route('/del_product/<path:url>')
def del_product(url):
    customer = Customer.query.filter(Customer.user == current_user).first()
    cart = Cart.query.filter(Cart.customer == customer).first()
    product = Product.query.filter(Product.url == url).first()
    cart_product = CartProduct.query.filter(CartProduct.cart.contains(cart),
                                            CartProduct.product == product.id).first()
    db.session.delete(cart_product)
    db.session.commit()

    return redirect(url_for('.get_cart'))

@cart.route('/change_quantity/<path:url>', methods=['POST'])
def change_quantity(url):
    customer = Customer.query.filter(Customer.user == current_user).first()
    cart = Cart.query.filter(Cart.customer == customer).first()
    product = Product.query.filter(Product.url == url).first()
    cart_product = CartProduct.query.filter(CartProduct.cart.contains(cart),
                                            CartProduct.product == product.id).first()
    q = int(request.form.get('quantity'))

    if bool(request.form.get('add_quantity')):
        q += 1
        cart_product.quantity = q
        cart_product.final_price = q * product.price

        db.session.add(cart_product)

    if bool(request.form.get('remove_quantity')):
        if q > 1:
            q -= 1
            cart_product.quantity = q
            cart_product.final_price = q * product.price

            db.session.add(cart_product)
        else:
            db.session.delete(cart_product)

    cart.final_price = sum([i.final_price for i in cart.cart_products])

    db.session.commit()

    return redirect(url_for('.get_cart'))


@cart.route('/order', methods=['POST', 'GET'])
@login_required
def order():

    form = OrderForm()
    if form.validate_on_submit():
        customer = Customer.query.filter(Customer.user == current_user).first()
        cart = Cart.query.filter(Cart.customer == customer).first()

        order = Order(
            customer=customer.id,
            cart=cart.id,
            number=randint(1, 9999),
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            delivery=form.delivery.data,
            address=form.address.data)

        db.session.add(order)
        db.session.commit()

        return render_template('order_end.html', order=order)

    return render_template('order_start.html', form=form)

