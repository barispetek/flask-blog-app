from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import RegisterForm, LoginForm, PostForm
from app.models import User, Post
from app import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return redirect(url_for("main.login"))

@main_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash("Username already exists.", "error")
            return redirect(url_for("main.register"))

        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. You can now log in.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)

@main_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("main.dashboard"))
        flash("Invalid username or password.", "error")
    return render_template("login.html", form=form)

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.login"))

@main_bp.route("/dashboard")
@login_required
def dashboard():
    search_query = request.args.get("q")
    if search_query:
        posts = Post.query.filter(Post.user_id == current_user.id, Post.title.ilike(f"%{search_query}%"))\
                          .order_by(Post.created_at.desc()).all()
    else:
        posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts, search_query=search_query)

@main_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id
        )
        db.session.add(new_post)
        db.session.commit()
        flash("Post created successfully!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("create_post.html", form=form)

@main_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.filter_by(id=post_id, user_id=current_user.id).first_or_404()
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post updated successfully!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("edit_post.html", form=form, post=post)

@main_bp.route("/post/<int:post_id>")
@login_required
def post_detail(post_id):
    post = Post.query.filter_by(id=post_id, user_id=current_user.id).first_or_404()
    return render_template("post_detail.html", post=post)

@main_bp.route("/delete/<int:post_id>", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id, user_id=current_user.id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully!", "warning")
    return redirect(url_for("main.dashboard"))