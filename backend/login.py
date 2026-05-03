from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from database import get_db_connection

login_bp = Blueprint('login', __name__)

def user_authenticate(email, password):
    connection = get_db_connection()

    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT user_id, name, email, user_type, password_hash
            FROM users
            WHERE email = %s
        """

        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password_hash'], password):
            return {
                'user_id': user['user_id'],
                'name': user['name'],
                'email': user['email'],
                'user_type': user['user_type']
            }

        return None

    except Exception as error:
        print("Login error:", error)
        return None

    finally:
        cursor.close()
        connection.close()


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({
            'message': 'Email and password are required'
        }), 400

    user = user_authenticate(email, password)

    if user:
        return jsonify({
            'message': 'Login successful',
            'user': user
        }), 200

    return jsonify({
        'message': 'Invalid email or password'
    }), 401