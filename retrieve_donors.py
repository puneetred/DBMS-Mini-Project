import streamlit as st
import mysql.connector

def retrieve_donors_page():
    st.subheader("Retrieve All Donors")

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    # Retrieve all donors from the database
    query = "SELECT * FROM donors"
    cursor.execute(query)
    donors = cursor.fetchall()

    # Display the retrieved donors
    if donors:
        st.subheader("Donors")
        for donor in donors:
            st.container()
            col1, col2 = st.columns(2)
            col1.write(f"Name: {donor[1]}")
            col1.write(f"Blood Group: {donor[2]}")
            col1.write(f"Age: {donor[3]}")
            col1.write(f"Gender: {donor[4]}")
            col2.write(f"Contact Number: {donor[5]}")
            col2.write(f"Email: {donor[6]}")
            col2.write(f"Address: {donor[7]}")
            col2.write(f"Last Donation Date: {donor[8]}")
            st.write("---")
    else:
        st.info("No donors found!")

    # Close the database connection
    cursor.close()
    connection.close()
