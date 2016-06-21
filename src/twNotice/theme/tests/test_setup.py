# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from twNotice.theme.testing import TWNOTICE_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that twNotice.theme is properly installed."""

    layer = TWNOTICE_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if twNotice.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'twNotice.theme'))

    def test_browserlayer(self):
        """Test that ITwnoticeThemeLayer is registered."""
        from twNotice.theme.interfaces import (
            ITwnoticeThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ITwnoticeThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TWNOTICE_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['twNotice.theme'])

    def test_product_uninstalled(self):
        """Test if twNotice.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'twNotice.theme'))

    def test_browserlayer_removed(self):
        """Test that ITwnoticeThemeLayer is removed."""
        from twNotice.theme.interfaces import ITwnoticeThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITwnoticeThemeLayer, utils.registered_layers())
