from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySQL 데이터베이스 연결 설정

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://kwon001:Manoit123@killdeerdbserver.mysql.database.azure.com:3306/test'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=generate_password_hash(data['password'], method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid username or password!'}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(host='0.0.0.0', port=8000)
