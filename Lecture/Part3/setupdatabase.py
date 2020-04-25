from basic import db, Puppy

db.create_all()
sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

print(sam.id)
print(frank.id)

db.session.add(sam)
db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)
