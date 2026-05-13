# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Patient # type: ignore

app = Flask(__name__,template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scanEmotion.db'
app.config['SECRET_KEY'] = 'votre_clé_secrète'
db.init_app(app)

@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('indexx.html', patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        age = request.form['age']
        email = request.form['email']
        profession = request.form['profession']
        etat_civil = request.form['etat_civil']
        
        new_patient = Patient(nom=nom, prenom=prenom, age=age, email=email, profession=profession, etat_civil=etat_civil)
        db.session.add(new_patient)
        db.session.commit()
        flash('Patient ajouté avec succès !')
        return redirect(url_for('index'))
    return render_template('edit_patient.html', patient=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)
    if request.method == 'POST':
        patient.nom = request.form['nom']
        patient.prenom = request.form['prenom']
        patient.age = request.form['age']
        patient.email = request.form['email']
        patient.profession = request.form['profession']
        patient.etat_civil = request.form['etat_civil']
        
        db.session.commit()
        flash('Patient mis à jour avec succès !')
        return redirect(url_for('index'))
    return render_template('edit_patient.html', patient=patient)

@app.route('/delete/<int:id>')
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    flash('Patient supprimé avec succès !')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Création des tables lors du démarrage de l'application
    app.run(debug=True)
