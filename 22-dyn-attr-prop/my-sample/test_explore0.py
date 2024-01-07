import pytest
from explore0 import FrozenJSON
import json

@pytest.fixture
def raw_feed():
    return json.load(open('data/osconfeed.json'))


def test_len_speakers(raw_feed):
    feed = FrozenJSON(raw_feed)
    assert len(feed.Schedule.speakers) == 357
