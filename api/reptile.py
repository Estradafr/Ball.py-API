
from flask import ( Blueprint, redirect, request)
from . import models

bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

@bp.route('/', methods=['GET', 'POST'])
def index():
    # post route
    if request.method == 'POST':
        # create a new reptile in db
        new_reptile = models.Reptile(
            common_name = request.form['common_name'],
            scientific_name = request.form['scientific_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_fact = request.form['fun_fact']
        )
        
        # add or commit to the db
        models.db.session.add(new_reptile)
        models.db.session.commit()
        
        # redirect to the index page
        return redirect('/reptiles')
    
    # get route & find all
    found_reptiles = models.Reptile.query.all()
    
    # create empty dictionary with an empty list
    reptile_dictionary = {'reptiles': []}
    
    # loop through all reptiles and append (add) it to the list
    for reptile in found_reptiles:
        reptile_dictionary["reptiles"].append({
            'common_name': reptile.common_name,
            'scientific_name': reptile.scientific_name,
            'conservation_status': reptile.conservation_status,
            'native_habitat': reptile.native_habitat,
            'fun_fact': reptile.fun_fact
        })
     # return the dictionary as JSON (default)
    return reptile_dictionary

@bp.route('/<int:id>')
def show(id): 
    # find the reptile by their id
    reptile = models.Reptile.query.filter_by(id=id).first()

    # create a dictionary of the reptile's info
    reptile_dictionary = {
            'common_name': reptile.common_name,
            'scientific_name': reptile.scientific_name,
            'conservation_status': reptile.conservation_status,
            'native_habitat': reptile.native_habitat,
            'fun_fact': reptile.fun_fact
        }
    
    # return the dictionary as JSON (default)
    return reptile_dictionary