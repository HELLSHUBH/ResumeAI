from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from database import get_db_connection

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name = data.get('name')
    dob = data.get('dob')
    gender = data.get('gender')
    occupation = data.get('occupation')
    user_type = data.get('userType')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    if not name or not user_type or not email or not password or not confirm_password:
        return jsonify({
            'message': 'Name, user type, email, password, and confirm password are required'
        }), 400

    if password != confirm_password:
        return jsonify({
            'message': 'Password and confirm password do not match'
        }), 400

    connection = get_db_connection()

    if connection is None:
        return jsonify({
            'message': 'Database connection failed'
        }), 500

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({
                'message': 'Email already registered'
            }), 409

        password_hash = generate_password_hash(password)

        insert_query = """
            INSERT INTO users
            (name, dob, gender, occupation, user_type, email, password_hash)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (
            name,
            dob,
            gender,
            occupation,
            user_type,
            email,
            password_hash
        ))

        connection.commit()

        user_id = cursor.lastrowid

        return jsonify({
            'message': 'Signup successful',
            'user': {
                'user_id': user_id,
                'name': name,
                'email': email,
                'user_type': user_type
            }
        }), 201

    except Exception as error:
        print("Signup error:", error)

        return jsonify({
            'message': 'Signup failed'
        }), 500

    finally:
        cursor.close()
        connection.close()