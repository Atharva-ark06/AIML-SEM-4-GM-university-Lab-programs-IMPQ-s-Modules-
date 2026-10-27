from importlib import import_module
m=import_module("examples.ml.phase4.23_residuals")
def test_residuals(): assert m.residuals([10,12,8],[9,13,8])==[1,-1,0]