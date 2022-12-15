from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration
musiikki_bp = Blueprint(
    'musiikki', __name__,
)

@musiikki_bp.route('/musiikki', methods=['GET'])
def index():
    return render_template(
        'musiikki.html', selected = "Musiikki"
    )
