from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from your_form_file import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(nome=form.nome.data, email=form.email.data, idade=form.idade.data, senha=form.senha.data)
        db.session.add(user)
        db.session.commit()
        return 'Usuário registrado com sucesso!'
    return render_template('register.html', form=form)
