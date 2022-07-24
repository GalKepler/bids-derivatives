from pathlib import Path
from unittest import TestCase

from bids_derivatives.derivative import SingleSubjectDerivative
from tests.fixtures import TEST_DATA_PATH, TEST_SUBJECTS


class SingleDerivativeTestCase(TestCase):
    TEST_DATA_PATH = TEST_DATA_PATH
    TEST_SUBJECTS = TEST_SUBJECTS

    def setUp(self) -> None:
        return super().setUp()

    def test_base_directory(self):
        """
        Test that the base directory is set correctly.
        """
        for key, available_subjects in self.TEST_SUBJECTS.items():
            subjects = available_subjects.get("valid")
            for subject in subjects:
                derivative = SingleSubjectDerivative(
                    Path(self.TEST_DATA_PATH) / key, subject
                )
                self.assertTrue(
                    derivative.path == Path(self.TEST_DATA_PATH) / key
                )

    def test_valid_subjects(self):
        """
        Test that the subjects in the test data are valid.
        """
        for key, available_subjects in self.TEST_SUBJECTS.items():
            subjects = available_subjects.get("valid")
            for subject in subjects:
                derivative = SingleSubjectDerivative(
                    Path(self.TEST_DATA_PATH) / key, subject
                )
            self.assertTrue(derivative.participant_label == subject)

    def test_invalid_subjects(self):
        """
        Test that the subjects in the test data are invalid.
        """
        for key, available_subjects in self.TEST_SUBJECTS.items():
            valid_subject = available_subjects.get("valid")[0]
            subjects = available_subjects.get("invalid")
            for subject in subjects:
                with self.assertRaises(ValueError):
                    SingleSubjectDerivative(
                        Path(self.TEST_DATA_PATH)
                        / key
                        / f"sub-{valid_subject}",
                        subject,
                    )
