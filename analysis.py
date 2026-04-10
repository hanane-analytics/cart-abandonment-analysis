import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

# 1. Abandonment by shipping visibility step
abandonment_by_step = df.groupby('shipping_visibility_step')['purchase'].apply(
    lambda x: 1 - x.mean()
).reset_index()

# 2. Abandonment by shipping cost ratio
df['ratio_category'] = pd.cut(
    df['shipping_cost_ratio'],
    bins=[0, 0.1, 0.2, 0.3, 1],
    labels=['Low', 'Medium', 'High', 'Very High']
)
abandonment_by_ratio = df.groupby('ratio_category')['purchase'].apply(
    lambda x: 1 - x.mean()
)

# 3. Abandonment by device x shipping ratio
abandonment_device = df.groupby(
    ['device_type', 'ratio_category']
)['purchase'].apply(
    lambda x: 1 - x.mean()
).unstack()

# 4. Abandonment by hour
abandonment_by_hour = df.groupby('session_hour')['purchase'].apply(
    lambda x: 1 - x.mean()
).sort_index()

# 5. Abandonment by day
abandonment_by_day = df.groupby('day_of_week')['purchase'].apply(
    lambda x: 1 - x.mean()
).sort_index()

print("Shipping Visibility Step:\n", abandonment_by_step)
print("\nShipping Ratio:\n", abandonment_by_ratio)
print("\nDevice x Ratio:\n", abandonment_device)
print("\nBy Hour:\n", abandonment_by_hour)
print("\nBy Day:\n", abandonment_by_day)
