from core import db

print('Init Model for Startpage')


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    health = db.Column(db.Integer, default=0)

    def __repr__(self):
        return 'Model Unit with name {}'.format(self.name)
