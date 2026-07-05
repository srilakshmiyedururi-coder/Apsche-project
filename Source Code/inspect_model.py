import pickle
from pathlib import Path
m = pickle.load(open(Path('templates') / 'HDI.pkl','rb'))
print('feature_names_in_ =', getattr(m, 'feature_names_in_', None))
print('n_features_in_ =', getattr(m, 'n_features_in_', None))
print('coef shape =', getattr(m, 'coef_', None).shape if hasattr(m,'coef_') else None)
