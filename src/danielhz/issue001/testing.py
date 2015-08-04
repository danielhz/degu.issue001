# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import danielhz.issue001


class DanielhzIssue001Layer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=danielhz.issue001)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'danielhz.issue001:default')


DANIELHZ_ISSUE001_FIXTURE = DanielhzIssue001Layer()


DANIELHZ_ISSUE001_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DANIELHZ_ISSUE001_FIXTURE,),
    name='DanielhzIssue001Layer:IntegrationTesting'
)


DANIELHZ_ISSUE001_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DANIELHZ_ISSUE001_FIXTURE,),
    name='DanielhzIssue001Layer:FunctionalTesting'
)


DANIELHZ_ISSUE001_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DANIELHZ_ISSUE001_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DanielhzIssue001Layer:AcceptanceTesting'
)
