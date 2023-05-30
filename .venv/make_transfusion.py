import streamlit as st
import mysql.connector

def make_transfusion_page():
    st.subheader("Make Transfusion")

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Puneetjain1208@",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    # Transfusion form
    with st.form("make_transfusion_form"):
        st.write("Enter transfusion details:")
        recipient_id = st.text_input("Recipient ID")
        transfusion_date = st.date_input("Transfusion Date")

        # Retrieve the blood group of the recipient based on recipient_id
        blood_group_query = "SELECT blood_group FROM recipients WHERE recipient_id = %s"
        cursor.execute(blood_group_query, (recipient_id,))
        recipient = cursor.fetchone()
        blood_group = recipient[0] if recipient else None

        if blood_group:
            st.write("Recipient Blood Group:", blood_group)
        else:
            st.warning("Recipient ID not found. Please enter a valid Recipient ID.")

        submit_button = st.form_submit_button("Make Transfusion")

    # Handle form submission
    if submit_button and blood_group:
        # Check if the required blood is available in the inventory
        check_inventory_query = "SELECT quantity FROM blood_inventory WHERE blood_group = %s"
        cursor.execute(check_inventory_query, (blood_group,))
        inventory = cursor.fetchone()
        if inventory and inventory[0] > 0:
            # Insert transfusion details into the database
            insert_query = "INSERT INTO transfusions (recipient_id, blood_group, transfusion_date) VALUES (%s, %s, %s)"
            values = (recipient_id, blood_group, transfusion_date)
            cursor.execute(insert_query, values)
            connection.commit()

            st.success("Transfusion made successfully!")
        else:
            st.warning("Required blood not available in the inventory.")
            st.info("Please redirect to 'Find Donors' to search for donors with the required blood group.")

    # Close the database connection
    cursor.close()
    connection.close()
