from keycloak.aio.mixins import WellKnownMixin
from keycloak.openid_connect import PATH_WELL_KNOWN
from keycloak.openid_connect import KeycloakOpenidConnect as SyncKeycloakOpenidConnect

__all__ = ("KeycloakOpenidConnect",)


class KeycloakOpenidConnect(WellKnownMixin, SyncKeycloakOpenidConnect):
    def get_path_well_known(self):
        return PATH_WELL_KNOWN
