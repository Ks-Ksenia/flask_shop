from flask import Blueprint, render_template, request

from models import MainMenu, Submenu, Product
from forms import SortForm


menu = Blueprint('menu', __name__, template_folder='templates/menu', static_folder='static')

@menu.route('/')
def catalog():
    main_menu = MainMenu.query.order_by(MainMenu.id).all()
    return render_template('main_menu.html', menu=main_menu, title='Каталог')


@menu.route('/<path:url>')
def submenu(url):
    menu = MainMenu.query.filter(MainMenu.url == url).first_or_404()
    submenu = Submenu.query.filter(Submenu.main_menu_id == menu.id).order_by(Submenu.id).all()

    return render_template('submenu.html',  menu=submenu, title='Каталог')


@menu.route('/products/<path:url>/', methods=['POST', 'GET'])
def product_list(url):
    collection = Submenu.query.filter(Submenu.url == url).first_or_404()
    products = Product.query.filter(Product.collection == collection.id)
    category = MainMenu.query.filter(MainMenu.id == collection.main_menu_id).first()

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1


    form = SortForm()

    if form.validate_on_submit():
        if form.min_price.data:
            products = products.filter(Product.price >= int(form.min_price.data))

        if form.max_price.data:
            products = products.filter(Product.price <= int(form.max_price.data))

        if form.exist.data:
            products = products.filter(Product.availability == 'В наличие')

        if form.sort.data == 'price':
            products = products.order_by(Product.price)

        if form.sort.data == '-price':
            products = products.order_by(Product.price.desc())



    pages = products.paginate(page=page, per_page=1)



    print(request.query_string)
    st = str(request.query_string)

    return render_template('products_list.html', products=products, url=url,
                           collection=collection, category=category, form=form, pages=pages, st=st)


@menu.route('/product/<path:url>/') # прописывать артикул
def product_detail(url):
    product = Product.query.filter(Product.url == url).first_or_404()
    collection = Submenu.query.filter(Submenu.id == product.collection).first()
    category = MainMenu.query.filter(MainMenu.id == collection.main_menu_id).first()

    return render_template('product_detail.html', product=product, collection=collection, category=category)
