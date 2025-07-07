from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin):
    def __init__(self, id_, username, password):
        self.id = id_
        self.username = username
        self.password = password

# Database connection
def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn

# Load user for session management
@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    if user:
        return User(user["id"], user["username"], user["password"])
    return None

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)

        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
            conn.commit()
            flash("Registration successful. You can now log in.")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists.")
        finally:
            conn.close()

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            user_obj = User(user['id'], user['username'], user['password'])
            login_user(user_obj)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password.")

    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Dashboard – Show all posts of the current user
@app.route('/dashboard')
@login_required
def dashboard():
    search_query = request.args.get('q')

    conn = get_db_connection()

    if search_query:
        posts = conn.execute(
            "SELECT * FROM posts WHERE user_id = ? AND title LIKE ? ORDER BY created_at DESC",
            (current_user.id, f'%{search_query}%')
        ).fetchall()
    else:
        posts = conn.execute(
            "SELECT * FROM posts WHERE user_id = ? ORDER BY created_at DESC",
            (current_user.id,)
        ).fetchall()

    conn.close()
    return render_template('index.html', posts=posts, search_query=search_query)


# Create new post
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn = get_db_connection()
        conn.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", (title, content, current_user.id))
        conn.commit()
        conn.close()

        flash("Post created successfully!")
        return redirect(url_for('dashboard'))

    return render_template('create_post.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ? AND user_id = ?", (post_id, current_user.id)).fetchone()

    if not post:
        conn.close()
        flash("Post not found or unauthorized.")
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        new_title = request.form['title']
        new_content = request.form['content']
        conn.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (new_title, new_content, post_id))
        conn.commit()
        conn.close()
        flash("Post updated successfully!")
        return redirect(url_for('dashboard'))

    conn.close()
    return render_template('edit_post.html', post=post)

@app.route('/post/<int:post_id>')
@login_required
def post_detail(post_id):
    conn = get_db_connection()
    post = conn.execute("SELECT * FROM posts WHERE id = ? AND user_id = ?", (post_id, current_user.id)).fetchone()
    conn.close()

    if not post:
        flash("Post not found.")
        return redirect(url_for('dashboard'))

    return render_template('post_detail.html', post=post)

@app.route('/')
def home():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
