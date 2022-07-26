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

    def test_false_base_directory(self):
        """
        Test that the base directory is set correctly.
        """
        for key in self.TEST_SUBJECTS:
            with self.assertRaises(ValueError):
                BIDSDerivative(
                    os.path.join(self.TEST_DATA_PATH, key + "_false")
                )

    def test_analysis_title(self):
        """
        Test that the analysis title is set correctly.
        """
        for key in self.TEST_SUBJECTS:
            derivative = BIDSDerivative(os.path.join(self.TEST_DATA_PATH, key))
            self.assertTrue(isinstance(derivative.analysis_title, str))
            self.assertTrue(derivative.analysis_title.lower() == key)

    def test_representation(self):
        """
        Test that the representation is set correctly.
        """
        for key in self.TEST_SUBJECTS:
            derivative = BIDSDerivative(os.path.join(self.TEST_DATA_PATH, key))
            self.assertTrue(isinstance(str(derivative), str))
            self.assertTrue(
                str(derivative).lower() == f"{key} derivatives query"
            )

    def test_dataset_description_read(self):
        """
        Test that the dataset description is set correctly.
        """
        for key in self.TEST_SUBJECTS:
            derivative = BIDSDerivative(os.path.join(self.TEST_DATA_PATH, key))
            self.assertTrue(
                isinstance(derivative.dataset_description_path, Path)
            )
            self.assertTrue(isinstance(derivative.dataset_description, dict))

    def test_dataset_description_logging(self):
        """
        Test that the dataset description is set correctly.
        """
        for key in self.TEST_SUBJECTS:
            derivative = BIDSDerivative(os.path.join(self.TEST_DATA_PATH, key))
            dataset_content = derivative.validate_dataset_description()
            self.assertTrue(all(dataset_content.get("required")))

    def test_available_subjects(self):
        for key in self.TEST_SUBJECTS:
            valid_subjects = self.TEST_SUBJECTS[key]["valid"]
            derivative = BIDSDerivative(os.path.join(self.TEST_DATA_PATH, key))
            self.assertTrue(isinstance(derivative.subjects, list))
            self.assertTrue(len(derivative.subjects) == len(valid_subjects))
