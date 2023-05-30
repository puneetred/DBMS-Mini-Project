import streamlit as st
import mysql.connector
from datetime import date, timedelta

def add_recipient_page():
    st.subheader("Add Recipient")

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    # Add recipient form
    with st.form("add_recipient_form"):
        st.write("Enter recipient details:")
        name = st.text_input("Name")
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        
        # Define the date range for date_of_birth validation, default date is 18 years ago
        max_date = date.today() - timedelta(days=365 * 18)  # 18 years ago
        min_date = date.today() - timedelta(days=365 * 100)  # 100 years ago
        date_of_birth = st.date_input("Date of Birth", value=max_date, min_value=min_date, max_value=max_date)
        
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact_number = st.text_input("Contact Number")
        email = st.text_input("Email")
        address = st.text_input("Address")
        medical_history = st.text_area("Medical History")

        submit_button = st.form_submit_button("Add Recipient")

    # Handle form submission
    if submit_button:
        # Insert recipient details into the database
        insert_query = "INSERT INTO recipients (name, blood_group, date_of_birth, gender, contact_number, email, address, medical_history) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, blood_group, date_of_birth, gender, contact_number, email, address, medical_history)
        cursor.execute(insert_query, values)
        connection.commit()

        # Retrieve the recipient id of the recipient that was just added
        cursor.execute("SELECT LAST_INSERT_ID()")

        st.success("Recipient added successfully! Recipient ID: " + str(cursor.fetchone()[0]))

    # Close the database connection
    cursor.close()
    connection.close()
