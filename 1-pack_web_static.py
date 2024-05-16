#!/usr/bin/python3
"""
A  Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static
    """
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive = 'web_static_' + time + '.tgz'
        local('mkdir -p versions')
        create = local('tar -cvzf versions/{} web_static'.format(archive))
        if create is not None:
            return archive
        else:
            None
    except:
        return None
