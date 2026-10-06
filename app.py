from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


# Create tables
with app.app_context():
    db.create_all()


# CREATE USER
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    user = User(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created",
        "user": user.to_dict()
    }), 201


# GET ALL USERS
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify([
        user.to_dict()
        for user in users
    ])


# GET SINGLE USER
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)

    return jsonify(user.to_dict())


# UPDATE USER
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)

    data = request.get_json()

    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)

    db.session.commit()

    return jsonify({
        "message": "User updated",
        "user": user.to_dict()
    })


# DELETE USER
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "message": "User deleted"
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Flask CRUD API is running",
        "version": "1.0",
        "endpoints": [
            "/users",
            "/users/<id>"
        ]
    })


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
