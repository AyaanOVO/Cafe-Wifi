from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from form import Form, DeleteCafe
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap5(app)

app.secret_key = '3jl02k$ls0%ladj)3k'


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    map_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String, nullable=False)
    coffee_price = db.Column(db.String, nullable=False)


@app.route('/')
def all_shops():
    list_of_cafe_shop = Cafe.query.all()
    return render_template("home_page.html", list_of_shops=list_of_cafe_shop)


@app.route('/shop/<int:id>', methods=['GET', 'POST'])
def detail_shop(id):
    cafe = db.get_or_404(Cafe, id)
    return render_template("shop_detail.html", img_url=cafe.img_url, shop_name=cafe.name)


@app.route('/add-shop', methods=['POST', 'GET'])
def add_shop():
    form = Form()
    if form.validate_on_submit():
        new_cafe = Cafe(name=form.name.data, map_url=form.map_url.data, img_url=form.img_url.data, seats=form.seats.data, location=form.location.data, coffee_price=form.coffee_price.data, has_sockets=form.has_socket.data, has_toilet=form.has_toilet.data, has_wifi=form.has_wifi.data, can_take_calls=form.can_take_calls.data)
        db.session.add(new_cafe)
        db.session.commit()

    return render_template("add_shopp.html", form=form)


@app.route('/delete-shop', methods=['POST', 'GET'])
def delete_cafe():
    form = DeleteCafe()
    if form.validate_on_submit():
        cafe = db.get_or_404(Cafe, int(form.Cafe_id.data))
        db.session.delete(cafe)
        db.session.commit()
        return redirect(url_for('all_shops'))

    return render_template('delete_cafe.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)