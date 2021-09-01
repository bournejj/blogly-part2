"""Blogly application."""
from flask import Flask, request, render_template, redirect, flash, sessions
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, User, db, Post


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chickenzarecool21837'
app.config['DEBUG_TB_REDIRECTS'] = False

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()


@app.route('/')
def users_index():
    """redirects to list of all users"""

    # users = User.query.order_by(User.last_name, User.first_name).all()
    return redirect("/users")


@app.route('/users')
def list_users():
    """show list of all pets in db"""
    users = User.query.all()

    return render_template("User_list.html", users=users)


@app.route('/create_new_user', methods=["GET"])
def create_new_user():
    """shows a form for creating a new user"""

    return render_template("Create_new_user.html")


@app.route('/create_user', methods=["POST"])
def create_user():
    """handles the form"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    new_user = User(first_name=first_name,
                    last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/{new_user.id}")


@app.route("/<int:user_id>")
def show_user(user_id):
    """shows the details of a user"""

    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)


@ app.route("/<int:user_id>")
def edit_user(user_id):
    """shows a form for editing a user"""

    user = User.query.get_or_404(user_id)

    return render_template("edit_user.html", user=user)


@ app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)


@ app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """handles form data and updates the users details """

    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@ app.route('/users/<int:user_id>/posts/new')
def add_new_post(user_id):
    """shows a form for adding a post"""

    user = User.query.get_or_404(user_id)

    return render_template('add_post.html', user=user)


@ app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def handle_add_form(user_id):
    """ handles the form data and shows the post details"""

    user = User.query.get_or_404(user_id)

    new_post = Post(title=request.form["title"],
                    content=request.form["content"],
                    user=user)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/{user_id}")


@ app.route('/posts/<int:post_id>')
def show_post(post_id):

    post = Post.query.get_or_404(post_id)

    return render_template("show_post.html", post=post)


@ app.route('/post/<int:post_id>/edit')
def post_edit(post_id):
    """Show a form to edit an existing user"""

    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)


@ app.route('/posts/<int:post_id>/edit/update', methods=["POST"])
def update_post(post_id):
    """handles form data and updates the users details """

    post = Post.query.get_or_404(post_id)
    post.title = request.form["title"]
    post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()

    return redirect(f"/posts/{post.user_id}")
