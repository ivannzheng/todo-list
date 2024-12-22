from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    due_date = db.Column(db.Date, nullable=True)

    def serialize(self):
        if self.due_date:
            due_date = self.due_date.strftime('%Y-%m-%d')
        else:
            due_date = None

        return {
            "id": self.id,
            "name": self.name,
            "due_date": due_date,
        }

