from Main import app, db

if _name_ == '_main_':
    with app.app_context():
        db.create_all()   
    app.run(debug=True)