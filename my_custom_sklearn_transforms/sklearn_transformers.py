from sklearn.base import BaseEstimator, TransformerMixin

#TODO! Transform for other categorical columns
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

class TransformBalanceColumn(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def bin(self, row):
        if str(row) in ["NO_CHECKING", "NEGATIVE", "LOW", "HIGH"]:
            return row
        val = float(row)
        if val < 0:
            return "NEGATIVE"
        if val >=0 and val <= 200:
            return "LOW"
        if val >= 200:
            return "HIGH"
        return row

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        
        data[self.column] = data[self.column].apply(self.bin)
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data

class TransformSavingsColumn(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def bin(self, row):
        if str(row) in ["UNKNOWN", "LOW", "MEDIUM", "HIGH", "HIGHEST"]:
            return row
        val = float(row)
        if val <= 100:
            return "LOW"
        if val > 100 and val <= 500:
            return "MEDIUM"
        if val > 500 and val <= 1000:
            return "HIGH"
        if val > 1000:
            return "HIGHEST"
        return row

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        
        data[self.column] = data[self.column].apply(self.bin)
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data

class TransformEmploymentColumn(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def bin(self, row):
        if str(row) in ["LOW", "MEDIUM", "HIGH", "HIGHEST"]:
            return row
        val = float(row)
        if val <= 0:
            return "LOW"
        if val > 0 and val <= 4:
            return "MEDIUM"
        if val > 4 and val <= 7:
            return "HIGH"
        if val > 7:
            return "HIGHEST"
        return row

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        
        data[self.column] = data[self.column].apply(self.bin)
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data

class TransformFloatColumn(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def bin(self, row):
        try:
            return float(row)
        except:
            return 0.0

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        
        data[self.column] = data[self.column].apply(self.bin)
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data