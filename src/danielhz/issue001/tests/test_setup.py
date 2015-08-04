# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from danielhz.issue001.testing import DANIELHZ_ISSUE001_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that danielhz.issue001 is properly installed."""

    layer = DANIELHZ_ISSUE001_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if danielhz.issue001 is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('danielhz.issue001'))

    def test_browserlayer(self):
        """Test that IDanielhzIssue001Layer is registered."""
        from danielhz.issue001.interfaces import IDanielhzIssue001Layer
        from plone.browserlayer import utils
        self.assertIn(IDanielhzIssue001Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DANIELHZ_ISSUE001_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['danielhz.issue001'])

    def test_product_uninstalled(self):
        """Test if danielhz.issue001 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('danielhz.issue001'))
