import optparse
import os
import unittest
import warnings

import mock as mock

from initializer import Initializer


class test_initialize(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore")

    def tearDown(self):
        warnings.resetwarnings()

    def test_initialize(self):
        initializer = Initializer()
        initializer.execute(is_unit_test=True)
        self.assertIsNotNone(initializer.output_txt)
        self.assertTrue(os.path.exists(initializer.output_txt))

        # A second call to execute should work without exceptions
        initializer.execute(is_unit_test=True)
        self.assertTrue(os.path.exists(initializer.output_txt))

        # Remove the artifacts generated and check that they are gone
        os.remove(initializer.output_txt)
        self.assertTrue(not os.path.exists(initializer.output_txt))

    def test_initialize_with_no_options(self):
        old_parser = optparse.OptionParser
        try:
            optparse.OptionsParser = mock.MagicMock(spec=optparse.OptionParser)
            optparse.OptionParser.parse_args = lambda x: (None, [])
            initializer = Initializer()
            initializer.execute(is_unit_test=True)
            self.assertIsNotNone(initializer.output_txt)
            self.assertTrue(os.path.exists(initializer.output_txt))
            os.remove(initializer.output_txt)
            self.assertTrue(not os.path.exists(initializer.output_txt))
        except Exception as a:
            self.fail(a.message)
        finally:
            optparse.OptionsParser = old_parser

if __name__ == "__main__":
    unittest.main()