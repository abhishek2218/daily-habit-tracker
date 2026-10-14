import streamlit as st
import database
import ui_layout

# -----------------------------------------
# ARMAN'S MASTER INTEGRATION (ENTRY POINT)
# -----------------------------------------
if __name__ == "__main__":
    # 1. Blueprint Step 1: Initialize the database to prevent "Empty File" crashes[cite: 6]
    database.init_db()
    
    # 2. Blueprint Step 2: Load the frontend layout from Moksh's file[cite: 6]
    ui_layout.render_ui()