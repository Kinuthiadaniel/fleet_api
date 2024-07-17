from app import app
from models import db,Vehicle, User

with app.app_context():
    print('Deleting data...')

    Vehicle.query.delete()
    User.query.delete()
    print('creating data...')

    v1 = Vehicle(vin = "KBH 644Q" ,make = 'Mistubishi')
    v2 = Vehicle(vin = 'KBJ 104W', make = 'Mistubishi')

    u1 = User(name = "dan", email= "dan@gmail.com", password = '12345678')
    u2 = User(name="john", email="john@gmail.com", password= '12345678')

    vehicles = [v1, v2]
    users = [u1, u2]
    db.session.add_all(vehicles)
    db.session.add_all(users)
    db.session.commit()
    print('Seeding done')