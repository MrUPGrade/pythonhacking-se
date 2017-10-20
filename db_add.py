import db

user = db.ToDo(name='Some name')
db.session.add(user)
db.session.commit()