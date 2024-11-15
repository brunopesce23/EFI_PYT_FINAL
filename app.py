import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired
from forms import MarcaForm #Clase 13/8
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/celulares'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

from models import Equipo, User

from views import register_bp
register_bp(app)

# FORMULARIO
class EquipoForm(FlaskForm):
    modelo = StringField('Modelo', validators=[DataRequired()])
    almacenamiento = SelectField('Almacenamiento', choices=[
        ('64GB', '64 GB'),
        ('128GB', '128 GB'),
        ('256GB', '256 GB'),
        ('512GB', '512 GB')
    ], validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    bateria = StringField('Condicion Bateria', validators=[DataRequired()])
    precio = DecimalField('Precio USD', validators=[DataRequired()], places=2)
    stock = SelectField('Stock', choices=[
        ('Sí', 'Sí'),
        ('No', 'No')
    ], validators=[DataRequired()])
    imei = StringField('IMEI', validators=[DataRequired()])
    accesorio = StringField('Accesorio', validators=[DataRequired()])
    submit = SubmitField('Guardar')

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lista_celulares')
def lista_celulares():
    try:
        equipos = Equipo.query.all()
        return render_template('lista_celulares.html', equipos=equipos)
    except Exception as e:
        return f"Ocurrió un error al cargar el lista de celulares: {e}"

@app.route('/add_iphone', methods=['GET', 'POST'])
def add_equipo():
    form = EquipoForm()
    if form.validate_on_submit():
        try:
            equipo = Equipo(
                modelo=form.modelo.data,
                almacenamiento=form.almacenamiento.data,
                color=form.color.data,
                bateria=form.bateria.data,
                precio=form.precio.data,
                stock=form.stock.data,
                imei=form.imei.data,
                accesorio=form.accesorio.data
            )
            db.session.add(equipo)
            db.session.commit()
            return redirect(url_for('lista_celulares'))
        except Exception as e:
            return f"Ocurrió un error al guardar el producto: {e}"
    return render_template('add_equipo.html', form=form)

@app.route('/edit_iphone/<int:id>', methods=['GET', 'POST'])
def edit_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    form = EquipoForm(obj=equipo)
    if form.validate_on_submit():
        equipo.modelo = form.modelo.data
        equipo.almacenamiento = form.almacenamiento.data
        equipo.color = form.color.data
        equipo.bateria = form.bateria.data
        equipo.precio = form.precio.data
        equipo.stock = form.stock.data
        equipo.imei = form.imei.data
        equipo.accesorio = form.accesorio.data
        db.session.commit()
        return redirect(url_for('lista_celulares'))
    return render_template('add_equipo.html', form=form, title='Editar Celular')

@app.route('/delete_iphone/<int:id>')
def delete_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('lista_celulares'))

if __name__ == '__main__':
    app.run(debug=True)
