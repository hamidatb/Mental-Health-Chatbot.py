import pytest
import json
from project import get_positive_affirmation, get_calming_activity, get_mental_health_resources, track_mood, mood_history

def test_get_positive_affirmation():
    # Test if the get_positive_affirmation function returns a non-empty string.
    result = get_positive_affirmation()
    assert isinstance(result, str)
    assert len(result) > 0


def test_get_calming_activity():
    # Test if the get_calming_activity function returns a non-empty string.
    result = get_calming_activity()
    assert isinstance(result, str)
    assert len(result) > 0


def test_get_mental_health_resources():
    # Test if the get_mental_health_resources function returns a non-empty string,
    # and if the string can be parsed into a dictionary with more than one entry.
    result = get_mental_health_resources()
    assert isinstance(result, str)
    assert len(result) > 0
    resources = json.loads(result)
    assert isinstance(resources, dict)
    assert len(resources) > 0


def test_track_mood():
    # Test if the track_mood function adds an entry to the mood_history list,
    # and if the last entry in the list has the correct mood.
    initial_length = len(mood_history)
    mood = "happy"
    track_mood(mood)
    assert len(mood_history) == initial_length + 1
    assert mood_history[-1]["mood"] == mood
