from flask import render_template

from cookbook_ws import app, orm, db
from cookbook_ws.orm import RecipeType


@app.route("/")
def welcome():
    """
    Main entry point, this method returns the default page for the whole site.
    """
    recipe_types = db.session.query(RecipeType)
    return render_template("index.html", recipe_types=recipe_types)


@app.route("/random")
def random_recipe():
    """
    This method returns a sample recipe page.

    TODO: Once we've got the backend implemented, we can change this method to serve a random recipe.
    """
    recipe_types = db.session.query(RecipeType)
    return render_template("recipe_page.html", recipe_types=recipe_types)


@app.route("/reset")
def reset_db():
    """
    This method initializes the database.

    This is very, VERY, temporary.
    """

    orm.initialize()

    recipe_types = db.session.query(RecipeType)
    return render_template("recipe_page.html", recipe_types=recipe_types)