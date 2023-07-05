# Python Keycloak Client

![https://travis-ci.org/Peter-Slump/python-keycloak-client.svg?branch=master](https://travis-ci.org/Peter-Slump/python-keycloak-client.svg?branch=master)
![https://readthedocs.org/projects/python-keycloak-client/badge/?version=latest](https://readthedocs.org/projects/python-keycloak-client/badge/?version=latest)
![https://codecov.io/gh/Peter-Slump/python-keycloak-client/branch/master/graph/badge.svg](https://codecov.io/gh/Peter-Slump/python-keycloak-client/branch/master/graph/badge.svg)
![https://api.codeclimate.com/v1/badges/30e837f8c737b5b3e120/maintainability](https://api.codeclimate.com/v1/badges/30e837f8c737b5b3e120/maintainability)

![https://img.shields.io/pypi/l/python-keycloak-client.svg](https://img.shields.io/pypi/l/python-keycloak-client.svg)
![https://img.shields.io/pypi/v/python-keycloak-client.svg](https://img.shields.io/pypi/v/python-keycloak-client.svg)
![https://img.shields.io/pypi/wheel/python-keycloak-client.svg](https://img.shields.io/pypi/wheel/python-keycloak-client.svg)
![https://badges.gitter.im/Python-Keycloak/Client.svg](https://badges.gitter.im/Python-Keycloak/Client.svg)

Python Client for Keycloak identity and access management service

[Documentation](http://python-keycloak-client.readthedocs.io/en/latest/)

http://www.keycloak.org/

https://github.com/Peter-Slump/python-keycloak-client

# Development

Install development environment:

```bash
$ make install-python
```

## Writing docs

Documentation is written using Sphinx and maintained in the docs folder.

To make it easy to write docs Docker support is available.

First build the Docker container:

```bash
$ docker build . -f DockerfileDocs -t python-keycloak-client-docs
```

Run the container

```bash
$ docker run -v `pwd`:/src --rm -t -i -p 8050:8050 python-keycloak-client-docs
```

Go in the browser to http://localhost:8050 and view the documentation which get
refreshed and updated on every update in the documentation source.

## Create release

```bash
$ git checkout master
$ git pull
-- Update release notes --
$ bumpversion release
$ make deploy-pypi
$ bumpversion --no-tag patch
$ git push origin master --tags
```

# Release Notes

**unreleased**

**v0.3.0**

- Added support for Keycloak > 17.0
- Bug fix: remove `auth/` from the urls as it is no longer there

**v0.2.3**

- Bug fix: `client_class` on `KeycloakRealm` constructor (thanks to `pcaro <https://github.com/pcaro>`\_)
- Improve Keycloak Client (thanks to `ByJacob <https://github.com/ByJacob>`\_)

  - add delete in admin client
  - add manage groups in realm
  - add manage user roles
  - rename Roles to ClientRoles

**v0.2.2**

- Added support for UMA1 for Keycloak < 4.0
- Allow to query registered users (thanks to `aberres <https://github.com/aberres>`\_)

**v0.2.1**

- Including aio version in released package. (thanks to `mackeyja92 <https://github.com/mackeyja92>`\_)

**v0.2.0**

- Added async client based on aiohttp (thanks to `nkoshell <https://github.com/nkoshell>`\_)

**v0.1.4**

- Add support for password grant (thanks to `scranen <https://github.com/scranen>`\_)
- Bugfix: Prevent multiple values for keyword argument 'audience' in jwt.decode() (thanks to `eugenejo <https://github.com/eugenejo>`\_)
