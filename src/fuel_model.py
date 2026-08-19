import os
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

class FuelEfficiencyModel:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = LinearRegression()
        self.feature_cols = None

    def fit(self, X: pd.DataFrame, y: np.ndarray):
        self.feature_cols = X.columns.tolist()
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        X_scaled = self.scaler.transform(X[self.feature_cols])
        return self.model.predict(X_scaled)
