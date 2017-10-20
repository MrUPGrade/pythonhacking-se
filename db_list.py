import db

todos = db.session.query(db.ToDo).all()
for t in todos:
    print('id:', t.id, ' name: ', t.name)