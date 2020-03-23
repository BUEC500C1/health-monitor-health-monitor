import pytest
import json
import blood_pressure_monitor as bpm


def test_getbp():
    data = bpm.getBP()
    assert data['name'] == 'bp' and data['values']
