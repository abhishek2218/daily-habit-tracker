import plotly.express as px
import pandas as pd

# -----------------------------------------
# SIDDHARTH'S CHARTING MODULE
# -----------------------------------------
def plot_success_bar(df):
    # Blueprint Crash Prevention: Charting an empty/1-row dataframe crashes Plotly[cite: 15]
    if len(df) < 2:
        return "Not enough data to generate charts. Keep logging!"
        
    # 1. Filter the data to only show "Completed" habits
    completed_data = df[df["Status"] == "Completed"]
    
    # 2. Count how many times each habit was completed
    chart_data = completed_data["Habit"].value_counts().reset_index()
    chart_data.columns = ["Habit Name", "Days Completed"]
    
    # 3. Draw the actual Bar Chart
    fig = px.bar(chart_data, x="Habit Name", y="Days Completed", title="Most Successful Habits")
    
    return fig

def plot_timeline(df):
    # Blueprint Crash Prevention: Need at least 2 data points to draw a line
    if len(df) < 2:
        return "Not enough data for a timeline. Keep logging!"
        
    # 1. Filter for Completed habits
    completed_data = df[df["Status"] == "Completed"]
    
    # 2. Group by the exact Date and count how many habits were done that day
    timeline_data = completed_data.groupby("Date").size().reset_index(name="Total Completed")
    
    # 3. Draw the Line Graph
    fig = px.line(timeline_data, x="Date", y="Total Completed", title="Daily Momentum", markers=True)
    
    return fig