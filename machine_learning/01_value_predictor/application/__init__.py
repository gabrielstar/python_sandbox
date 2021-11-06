# this is to mark folder is a package
# here we can initialize app with libs and composing elements

from flask import Flask

# this is factory method
def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")  # where configuration of our app lives

    with app.app_context():
        # Include our Routes
        from . import routes

        app.register_blueprint(routes.api)
        return app
