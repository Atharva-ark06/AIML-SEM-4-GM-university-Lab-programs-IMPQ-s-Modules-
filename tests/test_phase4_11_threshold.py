from importlib import import_module
import pytest
m=import_module("examples.ml.phase4.21_threshold")
def test_threshold_labels(): assert m.predict_threshold([0.2,0.6,0.9],0.6)==[0,1,1]
def test_invalid_threshold():
    with pytest.raises(ValueError): m.predict_threshold([0.2],1.1)