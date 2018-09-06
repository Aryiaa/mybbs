from flask.blueprints import Blueprint

bp=Blueprint('cms',url_prefix='/cms')

@bp.route('/')
def index():
    return 'cms index'