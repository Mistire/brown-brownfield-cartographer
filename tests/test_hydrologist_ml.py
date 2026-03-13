import pytest
import os
from analyzers.python_dataflow import PythonDataFlowAnalyzer

def test_scikit_learn_detection(tmp_path):
    # Create a mock python file with ML patterns
    pfile = tmp_path / "model.py"
    pfile.write_text("""
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('data.csv')
model = LogisticRegression()
model.fit(df, y)
pred = model.predict(test_df)
df.to_csv('out.csv')
""")
    
    analyzer = PythonDataFlowAnalyzer()
    ios = analyzer.extract_io(str(pfile))
    
    methods = [io['method'] for io in ios]
    assert "read_csv" in methods
    assert "fit" in methods
    assert "predict" in methods
    assert "to_csv" in methods
    
    # Check types
    types = [io['type'] for io in ios]
    assert "source" in types # read_csv
    assert "transformation" in types # fit/predict
    assert "sink" in types # to_csv
