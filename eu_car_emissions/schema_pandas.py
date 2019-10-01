import numpy as np
import pandas as pd

schema = {
        "ID": "uint32",
        "MS": "category",
        "Mp": "category",
        "VFN": "category",
        "Mh": "category",
        "Man": "category",
        "MMS": "category",
        "TAN": "category",
        "T": "category",
        "Va": "category",
        "Ve": "category",
        "Mk": "category",
        "Cn": "category",
        "Ct": "category",
        "Cr": "category",
        "m (kg)": pd.Int16Dtype(), # Nullable Integer type from pandas
        "Mt": pd.Int16Dtype(),
        "Enedc (g/km)": pd.Int16Dtype(),
        "Ewltp (g/km)": pd.Int16Dtype(),
        "W (mm)": pd.Int16Dtype(),
        "At1 (mm)": pd.Int16Dtype(),
        "At2 (mm)": pd.Int16Dtype(),
        "Ft": "category",
        "Fm": "category",
        "ec (cm3)": pd.Int16Dtype(),
        "ep (KW)": pd.Int16Dtype(),
        "z (Wh/km)": pd.Int16Dtype(),
        "It": "category",
        "Ernedc (g/km)": "float32",
        "Erwltp (g/km)": "float32",
        "De": "float32",
        "Vf": pd.Int16Dtype(),
        "r": "uint32"
        }
