import pandas as pd

def get_overall_completion(df):
    
    #CRASH prevention:Check if file is completely empty first
    if df.empty:
        return 0.0
    
    total_logged=len(df)
    total_done=len(df[df["Status"]=="Completed"])
    
    rate=(total_done/total_logged)*100
    return rate

def get_most_missed(df):
    #1. Blieprint Crash Check: Is the file completely empty?
    if df.empty:
        return "No Data Yet"
    
    #2. Filter the spreadsheet to ONLY show rows where status is "Missed"
    missed_rows=df[df["Status"]=="Missed"]
    
    #3.Hidden Crash Check: What if they have a perfect score?
    if missed_rows.empty:
        return "Nothing missed yet!"
    
    #4. Count up the habits in the missed list
    counts =missed_rows["Habit"].value_counts()
    
    #5.index[0] just grabs the name of the #1 item on that counted list
    top_missed=counts.index[0]
    
    return top_missed

#Function 3:STREAK CALCULATOR
def calculate_streak(df, habit_name):
    
    #1.Blueprint Crash Check: Is the file completely empty?
    if df.empty:
        return 0
    
    #.Filter the spreadsheet to only show the specific habit Arman aska for
    habit_data=df[df["Habit"]==habit_name]
    
    #3.Hidden Crash Check:What if the file has data ,but they haven't logged this habit yet?
    if habit_data.empty:
        return 0
    
    #4.Blueprint Logic:Sort the dates from newest to oldest(descending)
    habit_data=habit_data.sort_values(by="Date",ascending=False)
    
    #5.Blueprint Logic:Loop through the rows and count the streak
    streak=0
    # .iterrows is just Pandas' was of reading the spreadsheet one row at a time
    for index, row in habit_data.iterrows():
        if row["Status"]=="Completed":
            streak=streak+1
        else:
            #The moment we hit a "Missed " day,the streak is broken.Stop the loop.
            break
        
    return streak    
     

#The TEST(Run at the very bottom of my file)
if __name__== "__main__":
#Load the new official filename
 df=pd.read_csv("habit_data.csv")

 final_score=get_overall_completion(df)
 biggest_struggle= get_most_missed(df)
 reading_streak=calculate_streak(df,"Read 10 Pages")
 print("Current Completion Rate:",final_score,"%")
 print("You need to work on:",biggest_struggle)
 print("Your current reading streak is:",reading_streak )
