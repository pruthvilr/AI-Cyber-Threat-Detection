import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

class ThreatProcessor:
    def __init__(self):
        self.encoder = LabelEncoder()
        self.scaler = StandardScaler()

    def preprocess(self, df, training=True):
        # Drop columns that are usually unique/useless for general patterns
        df = df.copy()
        
        # Encode categorical data (Protocol, Service, Flag)
        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if col != 'label':
                df[col] = self.encoder.fit_transform(df[col])
        
        # Split features and label
        if 'label' in df.columns:
            y = df['label'].apply(lambda x: 1 if x != 'normal' else 0)
            X = df.drop('label', axis=1)
            return X, y
        return df