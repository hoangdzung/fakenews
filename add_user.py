from app import db, user_datastore
user = user_datastore.create_user(email='admin@test.com', password='admin')
db.session.add(user)
db.session.commit()