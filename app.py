from flask import Flask, render_template, request, redirect, url_for

from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId

from forms import SerieForm

app = Flask(__name__)
app.config.from_object('configs')
mongo = PyMongo(app)

@app.route("/")
def index():
    series = mongo.db.series.find()
    return render_template("index.html", series=series)


@app.route("/series/add/", methods=['GET', 'POST'])
def add():
    form = SerieForm()
    if request.method == 'POST':
        mongo.db.series.insert(form.data)
        return redirect(url_for("index"))

    return render_template("add.html", form=form)


@app.route("/series/<serie_id>/edit/", methods=['GET', 'POST'])
def edit(serie_id):
    serie = mongo.db.series.find_one({'_id': ObjectId(serie_id)})
    form = SerieForm(**serie)
    if request.method == 'POST':
        serie.update(form.data)
	mongo.db.series.save(serie)
	return redirect(url_for("index"))

    return render_template("edit.html", form=form, serie=serie, serie_id=serie_id)


@app.route("/series/<serie_id>/rating/<rating>/", methods=['GET'])
def rating(serie_id):
    serie = mongo.db.series.find_one({'_id': ObjectId(serie_id)})
    serie['rating'] = rating
    mongo.db.series.save(serie)
    return {}




@app.route("/series/<int:serie_id>/delete/", methods=['POST'])
def delete(serie_id):
    return redirect("index")

if __name__ == "__main__":
    app.run(debug=True)
