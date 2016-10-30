import os
from charmhelpers.core.hookenv import resource_get, log, open_port
from charmhelpers.core.host import chdir
from jujubigdata import utils
from charmhelpers.core import unitdata


class TomEE(object):
    """
    This class manages the TomEE deployment.

    :param DistConfig dist_config: The configuration container object needed.
    """
    def __init__(self, dist_config=None):
        self.dist_config = dist_config or utils.DistConfig()

    def install(self):

        self.dist_config.add_users()
        self.dist_config.add_dirs()

        result = resource_get('tomee')
        if not result:
            log("Failed to fetch TomEE resource")
            return False

        unitdata.kv().set("tomeetarball", result)
        log("TomEE tarball path is {}".format(result))
        tomee_install_dir = self.dist_config.path('tomee_dir')
        with chdir(tomee_install_dir):
            utils.run_as('tomcat', 'tar', '-zxvf', '{}'.format(result))

        tomee_dirs = [f for f in os.listdir(tomee_install_dir)
                      if f.startswith('apache-tomee')]
        catalina_home = os.path.join(tomee_install_dir, tomee_dirs[0])
        with utils.environment_edit_in_place('/etc/environment') as env:
            env['CATALINA_HOME'] = catalina_home
        unitdata.kv().set("catalina_home", catalina_home)
        self.open_ports()
        return True

    def start(self):
        catalina_home = unitdata.kv().get("catalina_home")
        utils.run_as('tomcat', '{}/bin/startup.sh'.format(catalina_home))

    def open_ports(self):
        for port in self.dist_config.exposed_ports('tomee'):
            open_port(port)