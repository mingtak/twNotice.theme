# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import twNotice.theme


class TwnoticeThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=twNotice.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'twNotice.theme:default')


TWNOTICE_THEME_FIXTURE = TwnoticeThemeLayer()


TWNOTICE_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TWNOTICE_THEME_FIXTURE,),
    name='TwnoticeThemeLayer:IntegrationTesting'
)


TWNOTICE_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TWNOTICE_THEME_FIXTURE,),
    name='TwnoticeThemeLayer:FunctionalTesting'
)


TWNOTICE_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TWNOTICE_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TwnoticeThemeLayer:AcceptanceTesting'
)
