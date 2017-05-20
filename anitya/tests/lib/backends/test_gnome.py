# -*- coding: utf-8 -*-
#
# Copyright © 2014  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions
# of the GNU General Public License v.2, or (at your option) any later
# version.  This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.  You
# should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Any Red Hat trademarks that are incorporated in the source
# code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission
# of Red Hat, Inc.
#

'''
anitya tests for the custom backend.
'''

import unittest

import anitya.lib.backends.gnome as backend
import anitya.lib.model as model
from anitya.lib.exceptions import AnityaPluginException
from anitya.tests.base import Modeltests, create_distro, skip_jenkins


BACKEND = 'GNOME'


class GnomeBackendtests(Modeltests):
    """ custom backend tests. """

    @skip_jenkins
    def setUp(self):
        """ Set up the environnment, ran before every tests. """
        super(GnomeBackendtests, self).setUp()

        create_distro(self.session)
        self.create_project()

    def create_project(self):
        """ Create some basic projects to work with. """
        project = model.Project(
            name='evolution-data-server',
            homepage='https://git.gnome.org/browse/evolution-data-server/',
            backend=BACKEND,
        )
        self.session.add(project)
        self.session.commit()

        project = model.Project(
            name='fake',
            homepage='https://pypi.python.org/pypi/repo_manager_fake',
            backend=BACKEND,
        )
        self.session.add(project)
        self.session.commit()

        project = model.Project(
            name='gnome-control-center',
            homepage='https://git.gnome.org/browse/gnome-control-center/',
            backend=BACKEND,
        )
        self.session.add(project)
        self.session.commit()

    def test_custom_get_version(self):
        """ Test the get_version function of the gnome backend. """
        pid = 1
        project = model.Project.get(self.session, pid)
        exp = '3.17.2'
        obs = backend.GnomeBackend.get_version(project)
        self.assertEqual(obs, exp)

        pid = 2
        project = model.Project.get(self.session, pid)
        self.assertRaises(
            AnityaPluginException,
            backend.GnomeBackend.get_version,
            project
        )

        pid = 3
        project = model.Project.get(self.session, pid)
        exp = '3.16.2'
        obs = backend.GnomeBackend.get_version(project)
        self.assertEqual(obs, exp)

    def test_custom_get_versions(self):
        """ Test the get_versions function of the gnome backend. """
        pid = 1
        project = model.Project.get(self.session, pid)
        exp = [
            u'0.0.3', u'0.0.4', u'0.0.5', u'0.0.6', u'0.0.7', u'0.0.90',
            u'0.0.91', u'0.0.92', u'0.0.93', u'0.0.94', u'0.0.94.1', u'0.0.95',
            u'0.0.96', u'0.0.97', u'0.0.98', u'0.0.99', u'1.0.0', u'1.0.1',
            u'1.0.2', u'1.0.3', u'1.0.4', u'1.1.0', u'1.1.1', u'1.1.2',
            u'1.1.3', u'1.1.4', u'1.1.4.1', u'1.1.4.2', u'1.1.5', u'1.1.6',
            u'1.2.0', u'1.2.1', u'1.2.2', u'1.2.3', u'1.3.1', u'1.3.2',
            u'1.3.3', u'1.3.3.1', u'1.3.4', u'1.3.5', u'1.3.6', u'1.3.6.1',
            u'1.3.7', u'1.3.8', u'1.4.0', u'1.4.1', u'1.4.1.1', u'1.4.2',
            u'1.4.2.1', u'1.5.1', u'1.5.2', u'1.5.3', u'1.5.4', u'1.5.5',
            u'1.5.90', u'1.5.91', u'1.5.92', u'1.6.0', u'1.6.1', u'1.6.2',
            u'1.6.3', u'1.7.1', u'1.7.2', u'1.7.3', u'1.7.4', u'1.7.90',
            u'1.7.90.1', u'1.7.91', u'1.7.92', u'1.8.0', u'1.8.1', u'1.8.2',
            u'1.8.3', u'1.9.1', u'1.9.2', u'1.9.3', u'1.9.4', u'1.9.5',
            u'1.9.6', u'1.9.6.1', u'1.9.91', u'1.9.92', u'1.10.0', u'1.10.1',
            u'1.10.2', u'1.10.3', u'1.10.3.1', u'1.11.1', u'1.11.2', u'1.11.3',
            u'1.11.4', u'1.11.5', u'1.11.6', u'1.11.6.1', u'1.11.90',
            u'1.11.91', u'1.11.92', u'1.12.0', u'1.12.1', u'1.12.2', u'1.12.3',
            u'2.21.1', u'2.21.2', u'2.21.3', u'2.21.4', u'2.21.5', u'2.21.5.1',
            u'2.21.90', u'2.21.91', u'2.21.92', u'2.22.0', u'2.22.1',
            u'2.22.1.1', u'2.22.2', u'2.22.3', u'2.23.1', u'2.23.2', u'2.23.3',
            u'2.23.4', u'2.23.5', u'2.23.6', u'2.23.90', u'2.23.90.1',
            u'2.23.91', u'2.23.92', u'2.24.0', u'2.24.1', u'2.24.1.1',
            u'2.24.2', u'2.24.3', u'2.24.4', u'2.24.4.1', u'2.24.5', u'2.25.1',
            u'2.25.2', u'2.25.3', u'2.25.4', u'2.25.5', u'2.25.90', u'2.25.91',
            u'2.25.92', u'2.26.0', u'2.26.1', u'2.26.1.1', u'2.26.2',
            u'2.26.3', u'2.27.1', u'2.27.2', u'2.27.3', u'2.27.4', u'2.27.5',
            u'2.27.90', u'2.27.91', u'2.27.92', u'2.28.0', u'2.28.1',
            u'2.28.2', u'2.28.3', u'2.28.3.1', u'2.29.1', u'2.29.2', u'2.29.3',
            u'2.29.4', u'2.29.5', u'2.29.6', u'2.29.90', u'2.29.91',
            u'2.29.92', u'2.30.0', u'2.30.1', u'2.30.2', u'2.30.2.1',
            u'2.30.3', u'2.31.1', u'2.31.2', u'2.31.3', u'2.31.3.1', u'2.31.4',
            u'2.31.5', u'2.31.6', u'2.31.90', u'2.31.91', u'2.31.92',
            u'2.31.92.1', u'2.32.0', u'2.32.1', u'2.32.2', u'2.32.3',
            u'2.91.0', u'2.91.1', u'2.91.1.1', u'2.91.2', u'2.91.3', u'2.91.4',
            u'2.91.4.1', u'2.91.5', u'2.91.6', u'2.91.90', u'2.91.91',
            u'2.91.92', u'3.0.0', u'3.0.1', u'3.0.2', u'3.0.2.1', u'3.0.3',
            u'3.0.3.1', u'3.1.1', u'3.1.2', u'3.1.3', u'3.1.4', u'3.1.5',
            u'3.1.90', u'3.1.91', u'3.1.92', u'3.2.0', u'3.2.1', u'3.2.2',
            u'3.2.3', u'3.3.1', u'3.3.1.1', u'3.3.2', u'3.3.3', u'3.3.4',
            u'3.3.5', u'3.3.90', u'3.3.91', u'3.3.92', u'3.4.0', u'3.4.1',
            u'3.4.2', u'3.4.3', u'3.4.4', u'3.5.1', u'3.5.2', u'3.5.3',
            u'3.5.3.1', u'3.5.4', u'3.5.5', u'3.5.90', u'3.5.91', u'3.5.92',
            u'3.6.0', u'3.6.1', u'3.6.2', u'3.6.3', u'3.6.4', u'3.7.1',
            u'3.7.2', u'3.7.2.1', u'3.7.3', u'3.7.4', u'3.7.5', u'3.7.90',
            u'3.7.91', u'3.7.92', u'3.8.0', u'3.8.1', u'3.8.2', u'3.8.3',
            u'3.8.4', u'3.8.5', u'3.9.1', u'3.9.2', u'3.9.3', u'3.9.4',
            u'3.9.5', u'3.9.90', u'3.9.91', u'3.9.92', u'3.10.0', u'3.10.1',
            u'3.10.2', u'3.10.3', u'3.10.4', u'3.11.1', u'3.11.2', u'3.11.3',
            u'3.11.4', u'3.11.5', u'3.11.90', u'3.11.91', u'3.11.92',
            u'3.12.0', u'3.12.1', u'3.12.2', u'3.12.3', u'3.12.4', u'3.12.5',
            u'3.12.6', u'3.12.7', u'3.12.7.1', u'3.12.8', u'3.12.9',
            u'3.12.10', u'3.12.11', u'3.13.1', u'3.13.2', u'3.13.3', u'3.13.4',
            u'3.13.5', u'3.13.6', u'3.13.7', u'3.13.8', u'3.13.9',
            u'3.13.10', u'3.13.90', u'3.15.91', u'3.15.92', u'3.16.0',
            u'3.16.1', u'3.16.2', u'3.17.1', u'3.17.2',
        ]
        obs = backend.GnomeBackend.get_ordered_versions(project)
        self.assertEqual(obs, exp)

        pid = 2
        project = model.Project.get(self.session, pid)
        self.assertRaises(
            AnityaPluginException,
            backend.GnomeBackend.get_versions,
            project
        )

        pid = 3
        project = model.Project.get(self.session, pid)
        exp = [
            u'2.19.1', u'2.19.3', u'2.19.4', u'2.19.5', u'2.19.6', u'2.19.90',
            u'2.19.91', u'2.19.92', u'2.20.0', u'2.20.0.1', u'2.20.1',
            u'2.20.3', u'2.21.1', u'2.21.2', u'2.21.4', u'2.21.5', u'2.21.90',
            u'2.21.92', u'2.22.0', u'2.22.1', u'2.22.2', u'2.22.2.1',
            u'2.23.1', u'2.23.2', u'2.23.3', u'2.23.4', u'2.23.5', u'2.23.6',
            u'2.23.90', u'2.24.0', u'2.24.0.1', u'2.25.1', u'2.25.2',
            u'2.25.3', u'2.25.90', u'2.25.92', u'2.26.0', u'2.27.3', u'2.27.4',
            u'2.27.4.1', u'2.27.5', u'2.27.90', u'2.27.91', u'2.28.0',
            u'2.28.1', u'2.29.4', u'2.29.6', u'2.29.90', u'2.29.91',
            u'2.29.92', u'2.30.0', u'2.30.1', u'2.31.1', u'2.31.2', u'2.31.3',
            u'2.31.4', u'2.31.4.1', u'2.31.4.2', u'2.31.5', u'2.31.6',
            u'2.31.90', u'2.31.91', u'2.31.92', u'2.31.92.1', u'2.32.0',
            u'2.32.1', u'2.90.1', u'2.91.0', u'2.91.2', u'2.91.3', u'2.91.3.1',
            u'2.91.4', u'2.91.5', u'2.91.6', u'2.91.90', u'2.91.91',
            u'2.91.92', u'2.91.93', u'3.0.0', u'3.0.0.1', u'3.0.1', u'3.0.1.1',
            u'3.0.2', u'3.1.3', u'3.1.4', u'3.1.5', u'3.1.90', u'3.1.91',
            u'3.1.92', u'3.2.0', u'3.2.1', u'3.2.2', u'3.2.3', u'3.3.2',
            u'3.3.3', u'3.3.4', u'3.3.4.1', u'3.3.5', u'3.3.90', u'3.3.91',
            u'3.3.92', u'3.4.0', u'3.4.1', u'3.4.2', u'3.4.3', u'3.4.3.1',
            u'3.5.2', u'3.5.3', u'3.5.4', u'3.5.5', u'3.5.6', u'3.5.90',
            u'3.5.91', u'3.5.92', u'3.6.0', u'3.6.1', u'3.6.2', u'3.6.3',
            u'3.7.1', u'3.7.3', u'3.7.4', u'3.7.5', u'3.7.5.1', u'3.7.90',
            u'3.7.91', u'3.7.92', u'3.8.0', u'3.8.1', u'3.8.1.5', u'3.8.2',
            u'3.8.3', u'3.8.4', u'3.8.4.1', u'3.8.5', u'3.8.6', u'3.9.2',
            u'3.9.2.1', u'3.9.3', u'3.9.5', u'3.9.90', u'3.9.90.1', u'3.9.91',
            u'3.9.92', u'3.10.0', u'3.10.1', u'3.10.2', u'3.10.3', u'3.10.4',
            u'3.11.1', u'3.11.2', u'3.11.3', u'3.11.5',
            u'3.11.90', u'3.11.91', u'3.11.92',
            u'3.12.0', u'3.12.1',
            u'3.13.1', u'3.13.2', u'3.13.3', u'3.13.4',
            u'3.13.90', u'3.13.91', u'3.13.92',
            u'3.14.0', u'3.14.1', u'3.14.2', u'3.14.3', u'3.14.4', u'3.14.5',
            u'3.15.4', u'3.15.90', u'3.15.91', u'3.15.92',
            u'3.16.0', u'3.16.1', u'3.16.2',
        ]
        obs = backend.GnomeBackend.get_ordered_versions(project)
        self.assertEqual(obs, exp)


if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(GnomeBackendtests)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
