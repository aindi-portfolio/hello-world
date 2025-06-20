# We import the `Flask` and `jsonify` classes from the Flask library.
from app import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
# We create a Flask application by initializing the `app` object.
app = Flask('simple')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://leanatsarni:April2019@MacBookPro/school'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    birthdate = db.Column(db.Integer)
    address_id = db.Column(db.Integer)

# DROP TABLE IF EXISTS students;
# CREATE TABLE students (
#   id           serial PRIMARY KEY,
#   first_name   varchar(255) NOT NULL,
#   last_name    varchar(255) NOT NULL,
#   birthdate    date NOT NULL,
#   address_id   integer
# );

# We define a route `/students` that responds to GET requests.
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(Student)

if __name__ == '__main__':
    app.run(debug=True, port=8000) # Flask tries to run on port 5000 by default but it's sometimes occupied by a different function. Let's tell flask to utilize port 8000 instead