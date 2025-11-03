import pandas as pd

sf = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1],
    'C': [1, 2, 3, 4]
})

print(f'sf:\n{sf}\n\nsf.corr():\n{sf.corr()}')

