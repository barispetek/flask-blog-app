from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config

api_bp = Blueprint("api", __name__, url_prefix="/api")

def get_db_connection():
    conn = psycopg2.connect(
        dbname=Config.POSTGRES_DB,
        user=Config.POSTGRES_USER,
        password=Config.POSTGRES_PASSWORD,
        host=Config.POSTGRES_HOST,
        port=Config.POSTGRES_PORT
    )
    return conn

@api_bp.route("/posts", methods=["GET"])
@login_required
def get_posts():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        'SELECT id, title, content, created_at FROM "post" WHERE user_id = %s ORDER BY created_at DESC',
        (current_user.id,)
    )
    posts = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(posts)

@api_bp.route("/post/<int:post_id>", methods=["GET"])
@login_required
def get_post_detail(post_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        'SELECT id, title, content, created_at FROM "post" WHERE id = %s AND user_id = %s',
        (post_id, current_user.id)
    )
    post = cur.fetchone()
    cur.close()
    conn.close()

    if post is None:
        return jsonify({"error": "Post not found"}), 404

    return jsonify(post)

@api_bp.route("/posts", methods=["POST"])
@login_required
def create_post_api():
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title and content required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO "post" (title, content, user_id) VALUES (%s, %s, %s)',
        (data['title'], data['content'], current_user.id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Post created successfully'}), 201

@api_bp.route("/post/<int:post_id>", methods=["PUT"])
@login_required
def update_post(post_id):
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE "post" SET title = %s, content = %s WHERE id = %s AND user_id = %s',
        (title, content, post_id, current_user.id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Post updated successfully"})

@api_bp.route("/post/<int:post_id>", methods=["DELETE"])
@login_required
def delete_post(post_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM "post" WHERE id = %s AND user_id = %s', (post_id, current_user.id))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Post deleted successfully"})
