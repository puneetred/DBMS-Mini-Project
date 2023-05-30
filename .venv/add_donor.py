import streamlit as st
import mysql.connector
from datetime import date, timedelta

def add_donor_page():
    st.subheader("Add Donor")

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Puneetjain1208@",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    # Add donor form
    with st.form("add_donor_form"):
        st.write("Enter donor details:")
        name = st.text_input("Name")
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        
        # Define the date range for date_of_birth validation, default date is 18 years ago
        max_date = date.today() - timedelta(days=365 * 18)  # 18 years ago
        min_date = date.today() - timedelta(days=365 * 60)  # 60 years ago
        date_of_birth = st.date_input("Date of Birth", value=max_date, min_value=min_date, max_value=max_date)
        
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact_number = st.text_input("Contact Number")
        email = st.text_input("Email")
        address = st.text_input("Address")

        submit_button = st.form_submit_button("Add Donor")

    # Handle form submission
    if submit_button:
        # Insert donor details into the database
        insert_query = "INSERT INTO donors (name, blood_group, date_of_birth, gender, contact_number, email, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, blood_group, date_of_birth, gender, contact_number, email, address)
        cursor.execute(insert_query, values)
        connection.commit()

        st.success("Donor added successfully!")

    # Close the database connection
    cursor.close()
    connection.close()
