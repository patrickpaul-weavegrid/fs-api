from app import app
from app.api.fs_resource import get_fs_resource

@app.route('/', defaults={'path': '/'}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def get_resource(path):
    if not path.startswith('/'):
        path = '/' + path
    if not path.endswith('/'):
        path = path + '/'
    return get_fs_resource(path)
    