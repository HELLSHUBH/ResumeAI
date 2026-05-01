from flask import Blueprint, request, jsonify
from database import get_db_connection

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile/<int:user_id>", methods=["GET"])
def get_profile(user_id):
    connection = get_db_connection()

    if connection is None:
        return jsonify({"message": "Database connection failed"}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT user_id, name, email, dob, gender, occupation, user_type, created_at
            FROM users
            WHERE user_id = %s
        """

        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "User not found"}), 404

        if user.get("dob"):
            user["dob"] = str(user["dob"])

        if user.get("created_at"):
            user["created_at"] = str(user["created_at"])

        return jsonify({
            "message": "Profile fetched successfully",
            "user": user
        }), 200

    except Exception as error:
        print("Profile fetch error:", error)
        return jsonify({"message": "Could not fetch profile"}), 500

    finally:
        cursor.close()
        connection.close()


@profile_bp.route("/profile/<int:user_id>", methods=["PUT"])
def update_profile(user_id):
    data = request.get_json()

    name = data.get("name")
    dob = data.get("dob")
    gender = data.get("gender")
    occupation = data.get("occupation")

    if not name:
        return jsonify({"message": "Name is required"}), 400

    connection = get_db_connection()

    if connection is None:
        return jsonify({"message": "Database connection failed"}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        update_query = """
            UPDATE users
            SET name = %s,
                dob = %s,
                gender = %s,
                occupation = %s
            WHERE user_id = %s
        """

        cursor.execute(update_query, (
            name,
            dob if dob else None,
            gender if gender else None,
            occupation if occupation else None,
            user_id
        ))

        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "User not found or no changes made"}), 404

        cursor.execute("""
            SELECT user_id, name, email, dob, gender, occupation, user_type, created_at
            FROM users
            WHERE user_id = %s
        """, (user_id,))

        updated_user = cursor.fetchone()

        if updated_user.get("dob"):
            updated_user["dob"] = str(updated_user["dob"])

        if updated_user.get("created_at"):
            updated_user["created_at"] = str(updated_user["created_at"])

        return jsonify({
            "message": "Profile updated successfully",
            "user": updated_user
        }), 200

    except Exception as error:
        print("Profile update error:", error)
        return jsonify({"message": "Profile update failed"}), 500

    finally:
        cursor.close()
        connection.close()