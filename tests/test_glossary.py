import pytest
import json
import os

def test_glossary_json_structure():
    """
    Tests that a sample glossary entry JSON object has the required keys.
    This is for T-001-01.
    """
    # A sample JSON object representing a single glossary entry
    glossary_entry_json = """
    {
        "term": "Plant Resilience",
        "definition": "The ability of a plant to withstand and recover from stressors."
    }
    """

    try:
        entry = json.loads(glossary_entry_json)
    except json.JSONDecodeError:
        pytest.fail("The sample glossary entry is not valid JSON.")

    # Check for the presence of required keys
    required_keys = ["term", "definition"]
    for key in required_keys:
        assert key in entry, f"The key '{key}' is missing from the glossary entry."

def test_glossary_json_with_extra_fields():
    """
    Tests that a glossary entry with extra fields still passes validation.
    """
    glossary_entry_json = """
    {
        "term": "Stressor",
        "definition": "An environmental factor that can negatively impact a plant's growth or development.",
        "source": "T-001"
    }
    """

    try:
        entry = json.loads(glossary_entry_json)
    except json.JSONDecodeError:
        pytest.fail("The sample glossary entry is not valid JSON.")

    required_keys = ["term", "definition"]
    for key in required_keys:
        assert key in entry, f"The key '{key}' is missing from the glossary entry."

def test_missing_definition_fails():
    """
    Tests that a glossary entry missing the 'definition' key fails validation.
    """
    glossary_entry_json = """
    {
        "term": "Abiotic Stress"
    }
    """
    entry = json.loads(glossary_entry_json)
    assert "definition" not in entry # This is the condition for the test, but the check is below

    # We expect the check to fail, so we wrap it in pytest.raises
    with pytest.raises(AssertionError):
        required_keys = ["term", "definition"]
        for key in required_keys:
            assert key in entry, f"The key '{key}' is missing from the glossary entry."

def test_generated_glossary_file_structure():
    """
    Tests the structure of the generated glossary_draft.json file.
    This is for T-001-05.
    """
    glossary_path = "glossary_draft.json"

    assert os.path.exists(glossary_path), f"Glossary file not found at '{glossary_path}'"

    with open(glossary_path, 'r', encoding='utf-8') as f:
        try:
            glossary_data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"The glossary file at '{glossary_path}' is not valid JSON.")

    assert isinstance(glossary_data, list), "Glossary data should be a list of entries."

    required_keys = ["term", "definition"]
    for entry in glossary_data:
        assert isinstance(entry, dict), "Each glossary entry should be a dictionary."
        for key in required_keys:
            assert key in entry, f"The key '{key}' is missing from a glossary entry."
