import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("Data ANALYSIS BY VISUALIZATION - P107/data.csv")
df.sort_values(by=['level'])
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()