import streamlit as st
import datetime
import database # Adding Indranil's backend pipes
import analytics
import visuals

# -----------------------------------------
# MOKSH'S FRONTEND LAYOUT
# -----------------------------------------
def render_ui():
    st.title("Daily Habit Tracker")
    
    # Blueprint: Sidebar navigation menu[cite: 14]
    menu_choice = st.sidebar.radio("Navigation", ["Log Entry", "View Analytics Dashboard"])
    
    # -----------------------------------------
    # PAGE 1: LOG ENTRY
    # -----------------------------------------
    if menu_choice == "Log Entry":
        st.header("Log a New Habit")
        
        # Blueprint Crash Prevention: Date input blocking future dates[cite: 14]
        today = datetime.date.today()
        selected_date = st.date_input("Select Date", max_value=today)
        
        # Blueprint: Selectbox populated ONLY with the 5 global habits[cite: 13, 14]
        habit_list = [
            "Drink 2L Water", 
            "Exercise 30 mins", 
            "Read 10 Pages", 
            "Code for 1 Hour", 
            "Sleep 8 Hours"
        ]
        selected_habit = st.selectbox("Choose Habit", habit_list)
        
        # Blueprint: Radio button for Status[cite: 14]
        selected_status = st.radio("Status", ["Completed", "Missed"])
        
        # Blueprint: Button to trigger the save action[cite: 14]
        if st.button("Save Entry"):
            #Connect the pipes:Pass Moksh'sfrontend variable into Indranil's backend function
            database.save_habit(str(selected_date),selected_habit,selected_status)
            #Show a green success message on the screen
            st.success(f"Successfully logged:{selected_habit} as {selected_status}!")
            
    # -----------------------------------------
    # PAGE 2: DASHBOARD
    # -----------------------------------------
    elif menu_choice == "View Analytics Dashboard":
        st.header("Your Progress")
        #1.Load the latest data from Indranil's database
        df=database.load_data()
        
        #2.Pass the data to your crash_proof math function
        completion_rate=analytics.get_overall_completion(df)
        
        #3.Blueprint:Display it on the screen using a metric card 
        st.metric(label="Overall Completion Rate",value=completion_rate)
         
        #4.Day 12:Display the raw pandas spreadsheet history
        st.write("### Habit History")
        st.dataframe(df)
        
        #5.Day 14:Render Siddharth's Bar Chart
        st.write("### Habit Success Chart")
        chart_result=visuals.plot_success_bar(df)
        
        #Crash-proof check:Did Siddharth return a warning string or a real Plotly figure?
        if isinstance(chart_result, str):
            st.warning(chart_result)
        else:
            st.plotly_chart(chart_result, use_container_width=True)    
         
        # Render Siddharth's Timeline Chart
        st.write("### Habit Momentum")
        timeline_result = visuals.plot_timeline(df)
        
        if isinstance(timeline_result, str):
            st.warning(timeline_result)
        else:
            st.plotly_chart(timeline_result, use_container_width=True) 
# -----------------------------------------
# PRIVATE TESTING ROOM
# -----------------------------------------
if __name__ == "__main__":
    render_ui()
