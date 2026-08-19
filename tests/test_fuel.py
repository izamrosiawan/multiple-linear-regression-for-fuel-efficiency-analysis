import pytest
import pandas as pd
import numpy as np
from src.fuel_model import FuelEfficiencyModel

def test_fuel_model_training_and_prediction():
    X = pd.DataFrame({
        'cylinders': [4, 6, 8, 4],
        'displacement': [140, 250, 350, 120],
        'horsepower': [80, 110, 160, 75],
        'weight': [2200, 3100, 4200, 2100]
    })
    y = np.array([28.0, 19.0, 14.0, 31.0])
    
    model = FuelEfficiencyModel()
    model.fit(X, y)
    preds = model.predict(X)
    
    assert len(preds) == 4
    # Mobil yang lebih berat harusnya memiliki MPG (efisiensi) yang lebih rendah
    assert preds[2] < preds[0]
