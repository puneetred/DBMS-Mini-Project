import streamlit as st
import mysql.connector

def add_donation_page():
    st.subheader("Add Donation")

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Puneetjain1208@",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    # Add donation form
    with st.form("add_donation_form"):
        st.write("Enter donation details:")
        donor_id = st.text_input("Donor ID")
        donation_date = st.date_input("Donation Date")

        submit_button = st.form_submit_button("Add Donation")

    # Retrieve the blood groups of the donor and recipient
    blood_group = get_blood_group(cursor, "donors", "donor_id", donor_id)

    # Handle form submission
    if submit_button:
        try:
            # Insert the donation record into the donations table
            insert_query = "INSERT INTO donations (donor_id, blood_group, donation_date) VALUES (%s, %s, %s)"
            values = (donor_id, blood_group, donation_date)
            cursor.execute(insert_query, values)
            connection.commit()

            st.success("Donation added successfully!")
        except mysql.connector.Error as error:
            st.error(f"Error occurred: {error}")

    # Close the database connection
    cursor.close()
    connection.close()

def get_blood_group(cursor, table, id_column, id_value):
    # Retrieve blood group based on the ID from the specified table
    query = f"SELECT blood_group FROM {table} WHERE {id_column} = %s"
    cursor.execute(query, (id_value,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
