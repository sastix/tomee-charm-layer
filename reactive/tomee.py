# pylint: disable=unused-argument
from charms.reactive import when, when_not, set_state
from charmhelpers.core.hookenv import status_set
from charms.layer.tomee import TomEE


@when_not('tomee.fetched')
def install_tomee():
    status_set('maintenance', 'installing Apache TomEE')
    tomee = TomEE()
    result = tomee.install()
    if not result:
        status_set("blocked", "Failed to fetch TomEE binary")
        return

    status_set('waiting', 'waiting for TomEE to start')
    set_state('tomee.installed')
    set_state('tomee.fetched')


@when_not('tomme.started')
@when('tomee.installed')
def start_tomee():
    status_set('maintenance', 'starting TomEE')
    tomee = TomEE()
    tomee.start()
    status_set('active', 'ready')
