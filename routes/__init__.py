from .login import login_bp
from .profile import profile_bp
from .register import register_bp
from .homepage import homepage_bp
from .logout import logout_bp

def register_routes(app):
    app.register_blueprint(login_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(homepage_bp)
    app.register_blueprint(logout_bp)