import pytest
from .transcriber import parse_ts

test_data = [
    ('120:34', {'is_ts': True, 'ts_val': '120:34'}),
    ('01:25', {'is_ts': True, 'ts_val': '01:25'}),
    ('00:00', {'is_ts': True, 'ts_val': '00:00'}),
    ('son by trade', {'is_ts': False, 'ts_val': None}),
]


@pytest.mark.parametrize('text_data,expected', test_data)
def test_parse_ts(text_data, expected):

    is_ts, ts_value = parse_ts(text_data)

    assert is_ts == expected.get('is_ts')
    assert ts_value == expected.get('ts_val')
