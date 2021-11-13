from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class EncodeColumns(BaseEstimator, TransformerMixin):
    def __init__(self, encoders, columns): # Respectivamente
        self.enc_col_dict = {col: encoders[i] for i, col in enumerate(columns)}
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        for col in self.enc_col_dict.keys():
            data[col] = self.enc_col_dict[col].transform(data[col])
        return data
