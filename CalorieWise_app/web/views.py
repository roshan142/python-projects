from flask import  Blueprint , render_template , request , redirect , url_for , flash
from flask_login import login_required,current_user
from .models import User_Data , Food , Log
from . import db
from datetime import datetime 

views = Blueprint("views",__name__)

@login_required
@views.route('/data-form', methods=['GET','POST'])
def data_form():
    if request.method == 'POST':
        weight = request.form.get('weight')
        height = request.form.get('height')
        calorie = request.form.get('calorie')
        protein = request.form.get('protein')
        carbs = request.form.get('carbs')
        fats = request.form.get('fats')
        data = User_Data(weight=weight, height=height,calorie=calorie,protein=protein,carbs=carbs,fats=fats,user_id=current_user.id)
        db.session.add(data)
        db.session.commit()

        return redirect(url_for('views.home'))
    return render_template('data_form.html')

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    logs = Log.query.order_by(Log.date.desc()).all()
    log_dates = []

    for log in logs:
        proteins = 0
        carbs = 0
        fats = 0
        calories = 0
        quantity = 1

        for food in log.foods:
            proteins += food.proteins
            carbs += food.carbs 
            fats += food.fats
            calories += food.calories
            quantity += food.quantity

        log_dates.append({
            'log_date' : log,
            'proteins' : proteins,
            'carbs' : carbs,
            'fats' : fats,
            'calories' : calories,
            'quantity' : quantity
        })
    return render_template('home.html', log_dates=log_dates)

@views.route('/create_log', methods=['POST'])
def create_log():
    date = request.form.get('date')
    log = Log(date=datetime.strptime(date, '%Y-%m-%d'))
    db.session.add(log)
    db.session.commit()
    return redirect(url_for('views.view', log_id=log.id))

@views.route('/delete_log/<int:log_id>')
def delete_log(log_id):
    log = Log.query.get_or_404(log_id)
    print(log)
    db.session.delete(log)
    db.session.commit()
    return redirect(url_for('views.home', log_id=log.id))
 
@login_required   
@views.route('/add')
def add():
    foods = Food.query.all()
    return render_template('add_food.html', foods=foods, food=None)

@views.route('/add', methods=['POST'])
def add_post():
    food_name = request.form.get('food-name').lower()
    quantity = request.form.get('quantity').lower()
    proteins = request.form.get('protein').lower()
    carbs = request.form.get('carbohydrates').lower()
    fats = request.form.get('fat').lower()
    food_id = request.form.get('food-id')
    
    foods = Food.query.all()
    counter = db.session.query(Food).filter(Food.name == food_name).count()
     
    if food_id:
        food = Food.query.get_or_404(food_id)
        food.name = food_name
        food.proteins = proteins
        food.carbs = carbs
        food.fats = fats  
        food.quantity = quantity
    elif counter >=1:
        flash('This Food Already Exist!', 'info')
        return redirect(url_for('views.add'))
    else:
        new_food = Food(
            name=food_name,
            proteins=proteins, 
            carbs=carbs, 
            fats=fats,
            quantity=quantity
        )
        db.session.add(new_food)
    db.session.commit()
    return redirect(url_for('views.add'))

@views.route('/delete_food/<int:food_id>')
def delete_food(food_id):
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    return redirect(url_for('views.add'))

@views.route('/edit_food/<int:food_id>')
def edit_food(food_id):
    food = Food.query.get_or_404(food_id)
    foods = Food.query.all()
    return render_template('add_food.html', food=food, foods=foods)
    
@views.route('/view/<int:log_id>', methods=['POST','GET'])
def view(log_id):
    log = Log.query.get_or_404(log_id)
    foods = Food.query.all()
    totals = {
        'protein' : 0,
        'carbs' : 0,
        'fat' : 0,
        'calories' : 0,
        'quantity': 1
    }

    for food in log.foods:
        totals['protein'] += food.proteins
        totals['carbs'] += food.carbs
        totals['fat'] += food.fats 
        totals['calories'] += food.calories
        totals['quantity'] += food.quantity
    return render_template('view_food.html', foods=foods, log=log, totals=totals)

@views.route('/add_food_to_log/<int:log_id>', methods=['POST'])
def add_food_to_log(log_id):
    try:
        log = Log.query.get_or_404(log_id)
        selected_food = request.form.get('food-select').lower()
        food = Food.query.get(int(selected_food)) 
        log.foods.append(food)
        db.session.commit()
        return redirect(url_for('views.view', log_id=log_id))
    except:
        flash('Only One Type of Food per day Allowed!', 'info')
        return redirect(url_for('views.view', log_id=log_id))

@views.route('/remove_food_from_log/<int:log_id>/<int:food_id>')
def remove_food_from_log(log_id, food_id):
    log = Log.query.get(log_id)
    food = Food.query.get(food_id)
    log.foods.remove(food)
    db.session.commit()
    return redirect(url_for('views.view', log_id=log_id))