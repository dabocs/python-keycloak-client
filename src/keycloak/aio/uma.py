from keycloak.aio.mixins import WellKnownMixin
from keycloak.uma import PATH_WELL_KNOWN
from keycloak.uma import KeycloakUMA as SyncKeycloakUMA

__all__ = ("KeycloakUMA",)


class KeycloakUMA(WellKnownMixin, SyncKeycloakUMA):
    def get_path_well_known(self):
        return PATH_WELL_KNOWN
