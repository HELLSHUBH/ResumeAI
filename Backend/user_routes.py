from flask import Blueprint, request, jsonify
from database import get_db_connection

user_bp = Blueprint('user', __name__)


@user_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    connection = get_db_connection()

    if connection is None:
        return jsonify({'message': 'Database connection failed'}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT user_id, name, email, dob, gender, occupation, user_type
            FROM users
            WHERE user_id = %s
        """, (user_id,))

        user = cursor.fetchone()

        if not user:
            return jsonify({'message': 'User not found'}), 404

        if user.get('dob'):
            user['dob'] = str(user['dob'])

        return jsonify({
            'user': user
        }), 200

    except Exception as error:
        print('Profile fetch error:', error)
        return jsonify({'message': 'Could not fetch profile'}), 500

    finally:
        cursor.close()
        connection.close()


@user_bp.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    data = request.get_json()

    name = data.get('name')
    dob = data.get('dob')
    gender = data.get('gender')
    occupation = data.get('occupation')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    connection = get_db_connection()

    if connection is None:
        return jsonify({'message': 'Database connection failed'}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            UPDATE users
            SET name = %s, dob = %s, gender = %s, occupation = %s
            WHERE user_id = %s
        """, (name, dob, gender, occupation, user_id))

        connection.commit()

        cursor.execute("""
            SELECT user_id, name, email, dob, gender, occupation, user_type
            FROM users
            WHERE user_id = %s
        """, (user_id,))

        user = cursor.fetchone()

        if user.get('dob'):
            user['dob'] = str(user['dob'])

        return jsonify({
            'message': 'Profile updated successfully',
            'user': user
        }), 200

    except Exception as error:
        print('Profile update error:', error)
        return jsonify({'message': 'Profile update failed'}), 500

    finally:
        cursor.close()
        connection.close()


@user_bp.route('/history/<int:user_id>', methods=['GET'])
def get_history(user_id):
    connection = get_db_connection()

    if connection is None:
        return jsonify({'message': 'Database connection failed'}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT 
                analysis_id,
                resume_file_name,
                job_description,
                match_score,
                matched_skills,
                missing_skills,
                feedback,
                suggestions,
                created_at
            FROM analysis_history
            WHERE user_id = %s
            ORDER BY created_at DESC
        """, (user_id,))

        history = cursor.fetchall()

        for item in history:
            if item.get('created_at'):
                item['created_at'] = str(item['created_at'])

        return jsonify({
            'history': history
        }), 200

    except Exception as error:
        print('History fetch error:', error)
        return jsonify({'message': 'Could not fetch history'}), 500

    finally:
        cursor.close()
        connection.close()