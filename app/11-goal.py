import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Team': ['Barcelona', 'Madrid', 
             'Sevilla', 'Madrid',
             'Barcelona', 'Sevilla', 
             'Madrid', 'Barcelona'],
    'Opponent': ['Sevilla', 'Barcelona', 
                 'Madrid', 'Sevilla', 
                 'Madrid', 'Barcelona', 
                 'Barcelona', 'Sevilla'],
    'Goals scored': np.random.randint(0, 5, size=8),
    'Goals conceded': np.random.randint(0, 5, size=8)
})

print('='*64)
print(df)


# Crate pivot table

pivot_table = df.pivot_table(values=['Goals scored','Goals conceded'],
                             index='Team', aggfunc=np.sum)
print(pivot_table)

