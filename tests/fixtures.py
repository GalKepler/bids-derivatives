import os

TESTS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
TEST_DATA_PATH = os.path.join(TESTS_DIRECTORY, "data")
TEST_SUBJECTS = {"qsiprep": {"valid": ["1"], "invalid": ["2"]}}
