from config import create_app

app = create_app(config_name='development')

from api.views.auth import shauri_blueprint
from api.views.products import shauri_blueprint

app.register_blueprint(shauri_blueprint, url_prefix = '/v2/api/')
