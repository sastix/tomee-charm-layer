#!/usr/bin/env python3

import unittest
import amulet


class TestDeploy(unittest.TestCase):
    """
    Trivial deployment test for Apache TomEE.
    """

    def test_deploy(self):
        self.d = amulet.Deployment(series='xenial')
        self.d.add('tomee', 'apache-tomee')
        self.d.setup(timeout=900)
        self.tomee = self.d.sentry['tomee'][0]
        self.d.sentry.wait_for_messages(
            {'tomee': 'Failed to fetch TomEE binary'}, timeout=1800)


if __name__ == '__main__':
    unittest.main()
