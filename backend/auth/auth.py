"""
Authentication Routes - JWT VERSION
"""

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from backend.database.db import db
from backend.database.models import User
import logging
import jwt
import datetime
import os

logger = logging.getLogger(__name__)

auth_bp = Blueprint("auth", __name__)


def generate_token(user_id: int) -> str:
    """Generate JWT token for user"""
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
<<<<<<< HEAD
=======
    
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    secret_key = os.environ.get("SECRET_KEY", "default-secret-key-change-in-production")
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

<<<<<<< HEAD

=======
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
def decode_token(token: str):
    """Decode and validate JWT token, returns payload or None"""
    try:
        secret_key = os.environ.get("SECRET_KEY", "default-secret-key-change-in-production")
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

<<<<<<< HEAD

@auth_bp.route("/register", methods=["POST"])
def register():
=======
@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Register new user
    """
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
<<<<<<< HEAD
            return jsonify({"error": "Username and password required"}), 400

        if len(password) < 6:
            return jsonify({"error": "Password must be at least 6 characters"}), 400

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return jsonify({"error": "Username already exists"}), 400
=======
            return jsonify(
                {"error": "Username and password required"}
            ), 400

        if len(password) < 6:
            return jsonify(
                {"error": "Password must be at least 6 characters"}
            ), 400

        existing_user = User.query.filter_by(
            username=username
        ).first()

        if existing_user:
            return jsonify(
                {"error": "Username already exists"}
            ), 400
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4

        user = User(
            username=username,
            password_hash=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        logger.info(f"New user registered: {username}")

<<<<<<< HEAD
        return jsonify({"message": "User registered successfully", "user_id": user.id}), 201
=======
        return jsonify(
            {"message": "User registered successfully", "user_id": user.id}
        ), 201
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4

    except Exception as e:
        db.session.rollback()
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500


@auth_bp.route("/login", methods=["POST"])
def login():
<<<<<<< HEAD
=======
    """
    Login user - returns JWT token
    """
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
<<<<<<< HEAD
            return jsonify({"error": "Username and password required"}), 400
=======
            return jsonify(
                {"error": "Username and password required"}
            ), 400
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4

        user = User.query.filter_by(username=username).first()

        if not user:
<<<<<<< HEAD
            return jsonify({"error": "Invalid credentials"}), 401

        if not check_password_hash(user.password_hash, password):
            return jsonify({"error": "Invalid credentials"}), 401

=======
            return jsonify(
                {"error": "Invalid credentials"}
            ), 401

        if not check_password_hash(user.password_hash, password):
            return jsonify(
                {"error": "Invalid credentials"}
            ), 401

        # Generate JWT token
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
        token = generate_token(user.id)

        logger.info(f"User logged in: {username}")

<<<<<<< HEAD
        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": user.to_dict()
        }), 200
=======
        return jsonify(
            {
                "message": "Login successful",
                "token": token,
                "user": user.to_dict()
            }
        ), 200
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4

    except Exception as e:
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500


@auth_bp.route("/logout", methods=["POST"])
def logout():
<<<<<<< HEAD
=======
    """
    Logout - JWT is stateless, just clear client-side token
    """
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    return jsonify({"message": "Logout successful. Clear token on client."}), 200


@auth_bp.route("/me", methods=["GET"])
def current_user():
<<<<<<< HEAD
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({"error": "No authorization header"}), 401

    try:
        token = auth_header.split(" ")[1]
        payload = decode_token(token)

        if not payload:
            return jsonify({"error": "Invalid or expired token"}), 401

        user_id = payload['user_id']
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({"user": user.to_dict()}), 200

=======
    """
    Get currently logged in user from JWT token
    """
    auth_header = request.headers.get('Authorization')
    
    if not auth_header:
        return jsonify({"error": "No authorization header"}), 401
    
    try:
        token = auth_header.split(" ")[1]  # "Bearer <token>"
        secret_key = os.environ.get("SECRET_KEY", "default-secret-key-change-in-production")
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user_id = payload['user_id']
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({"user": user.to_dict()}), 200
        
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    except Exception as e:
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500