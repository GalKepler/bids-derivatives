import os
from pathlib import Path
from unittest import TestCase

from bids_derivatives.dataset import BIDSDerivative
from tests.fixtures import TEST_DERIVATIVES_PATH, TEST_SUBJECTS


class BIDSDerivativeTestCase(TestCase):
    TEST_DATA_PATH = TEST_DERIVATIVES_PATH
    TEST_SUBJECTS = TEST_SUBJECTS

    def setUp(self) -> None:
        return super().setUp()

    def test_base_directory(self):
        """
        Test that the base directory is set correctly.
        """
        for key in self.TEST_SUBJECTS:
            derivative = BIDSDerivative(os.path.join(self.TEST_DATA_PATH, key))
            self.assertTrue(isinstance(derivative.base_directory, Path))

    def test_analysis_title(self):
        """
        Test that the analysis title is set correctly.
        """
        for key in self.TEST_SUBJECTS:
            derivative = BIDSDerivative(os.path.join(self.TEST_DATA_PATH, key))
            self.assertTrue(isinstance(derivative.analysis_title, str))
            self.assertTrue(derivative.analysis_title.lower() == key)
