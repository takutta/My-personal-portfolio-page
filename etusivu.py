from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration
etusivu_bp = Blueprint(
    'etusivu', __name__,
)

@etusivu_bp.route('/')
def index():
    return render_template(
        'etusivu.html', selected = "Minä"
    )

