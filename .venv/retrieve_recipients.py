import streamlit as st
import mysql.connector

def retrieve_recipients_page():
    st.subheader("Retrieve All Recipients")

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Puneetjain1208@",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    # Retrieve all recipients from the database
    query = "SELECT * FROM recipients"
    cursor.execute(query)
    recipients = cursor.fetchall()

    # Display the retrieved recipients in a table
    if recipients:
        st.table(recipients)
    else:
        st.info("No recipients found!")

    # Close the database connection
    cursor.close()
    connection.close()
