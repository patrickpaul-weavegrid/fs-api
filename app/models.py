from fs.osfs import OSFS
from os import environ
import atexit
import mimetypes


class FSResource:
    def __init__(self):
        self.fs_root = environ.get('ROOT_PATH')
        if not self.fs_root.endswith('/'):
            self.fs_root = self.fs_root + '/'

        self.root_fs = OSFS(self.fs_root)
        atexit.register(self.cleanup)

    def is_dir(self, path):
        dir = self.root_fs.scandir(path, namespaces=['details', 'access'])
        dir_dict = {}
        dir_dict_raw = {}
        for val in dir:
            dir_dict_raw[val.name] = val.raw
            filename = dir_dict_raw[val.name]['basic']['name']

            dir_dict[filename] = {}
            dir_dict[filename]['file'] = {}

            dir_dict[filename]['file']['name'] = filename
            dir_dict[filename]['file']['owner'] = dir_dict_raw[filename]['access']['user']
            dir_dict[filename]['file']['size'] = dir_dict_raw[filename]['details']['size']

            syspath = self.fs_root + path + \
                filename
            inroot_path = path + filename
            if self.root_fs.isdir(inroot_path):
                dir_dict[filename]['file']['type'] = 'Directory'
            elif self.root_fs.isfile(inroot_path):
                filetype, _ = mimetypes.guess_type(syspath)
                if not filetype:
                    filetype = 'Unknown File Type'
                dir_dict[filename]['file']['type'] = filetype

        return dir_dict

    def is_file(self, path):
        info = self.root_fs.getinfo(path, namespaces=['details', 'access'])
        info_dict = info.raw
        filename = info.raw['basic']['name']
        max_request_bytes = 1024
        info_dict = {}
        with self.root_fs.open(path) as req_file:
            req_file_content = req_file.read(max_request_bytes)
        info_dict['file'] = {}
        info_dict['file']['name'] = filename
        info_dict['file']['text'] = req_file_content
        return info_dict

    def cleanup(self):
        self.root_fs.close()
