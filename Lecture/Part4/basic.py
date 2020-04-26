from models import db, Puppy, Owner, Toy

# CREATING TWO PUPPIES
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD PUPPIES TO DATABASE
db.session.add(rufus)
db.session.add(fido)
db.session.commit()

# Check !
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create owner object
jose = Owner('Jose',rufus.id)

#Give toys to Rufus
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add(jose)
db.session.add(toy1)
db.session.add(toy2)
db.session.commit()

# GRAB RUFUS AGAIN
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()

