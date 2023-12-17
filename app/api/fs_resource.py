from flask import request
from app.api import bp
from app.api.errors import bad_request
from app.models import FSResource


@bp.route('', methods=['POST'])
def get_fs_resource(path):
    fs_resource = FSResource()

    if not fs_resource.root_fs.exists(path):
        return bad_request('requested path does not exist - %s entered' % path)

    if not fs_resource.root_fs.exists(path):
        return bad_request('requested path does not exist - %s entered' % path)

    if fs_resource.root_fs.isdir(path):
        return fs_resource.is_dir(path)

    if fs_resource.root_fs.isfile(path):
        return fs_resource.is_file(path)
