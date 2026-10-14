import pandas as pd
import os

# -----------------------------------------
# FUNCTION 1: INITIALIZE DATABASE
# -----------------------------------------
def init_db():
    # Blueprint: Check if habit_data.csv exists. If no, create it with headers.
    if not os.path.exists("habit_data.csv"):
        # We create a totally empty spreadsheet but give it the 3 required column names
        empty_df = pd.DataFrame(columns=["Date", "Habit", "Status"])
        empty_df.to_csv("habit_data.csv", index=False)
        print("System: Created a fresh habit_data.csv file.")
    else:
        print("System: Database already exists. Safe to proceed.")

# -----------------------------------------
# FUNCTION 2: SAVE A HABIT
# -----------------------------------------
def save_habit(date_str, habit_str, status_str):
    # Blueprint Crash Prevention: Reject if status isn't exactly "Completed" or "Missed"
    if status_str != "Completed" and status_str != "Missed":
        print("CRASH PREVENTED: Invalid status received.")
        return 
        
    # Create a tiny 1-row spreadsheet for the new data
    new_data = pd.DataFrame({
        "Date": [date_str],
        "Habit": [habit_str],
        "Status": [status_str]
    })
    
    # Blueprint: Open CSV in 'append' mode (mode='a') so it adds to the bottom instead of overwriting
    # header=False prevents it from writing the words "Date, Habit, Status" in the middle of our data
    new_data.to_csv("habit_data.csv", mode='a', header=False, index=False)
    print(f"Success: Saved {habit_str} as {status_str}.")

# -----------------------------------------
# FUNCTION 3: LOAD THE DATA
# -----------------------------------------
def load_data():
    # Always make sure the database exists before trying to read it
    init_db()
    
    # Blueprint: Uses pandas.read_csv() to read the file
    df = pd.read_csv("habit_data.csv")
    
    # Blueprint: Converts the 'Date' column to actual Pandas datetime objects
    if not df.empty:
        df["Date"] = pd.to_datetime(df["Date"])
        
    return df

# -----------------------------------------
# INDRANIL'S PRIVATE TESTING ROOM
# -----------------------------------------
if __name__ == "__main__":
    # 1. Test the startup function
    init_db()
    
    # 2. Test saving a valid habit
    save_habit("2026-10-14", "Code for 1 Hour", "Completed")
    
    # 3. Test saving an INVALID habit to prove the crash prevention works
    save_habit("2026-10-15", "Read 10 Pages", "I forgot")
    
    # 4. Test loading the data
    final_data = load_data()
    print("\nHere is the final database:")
    print(final_data)