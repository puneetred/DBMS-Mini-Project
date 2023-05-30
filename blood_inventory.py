import streamlit as st
import mysql.connector

def add_donation(donor_id, blood_group, donation_date):
    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    try:
        # Insert the donation record into the donations table
        insert_query = "INSERT INTO donations (donor_id, blood_group, donation_date) VALUES (%s, %s, %s)"
        values = (donor_id, blood_group, donation_date)
        cursor.execute(insert_query, values)

        # Update the blood inventory
        update_query = "UPDATE blood_inventory SET quantity = quantity + 1 WHERE blood_group = %s"
        cursor.execute(update_query, (blood_group,))

        connection.commit()
        st.success("Donation recorded successfully!")
    except mysql.connector.Error as error:
        st.error(f"Error occurred: {error}")
    finally:
        # Close the database connection
        cursor.close()
        connection.close()

def inventory_page(filter_blood_group=None):
    st.subheader("Blood Inventory")

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Puneetjain1208@",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    # Retrieve blood inventory from the database
    query = "SELECT blood_group, quantity FROM blood_inventory"
    if filter_blood_group:
        query += " WHERE blood_group = %s"
        cursor.execute(query, (filter_blood_group,))
    else:
        cursor.execute(query)
    inventory = cursor.fetchall()

    # Display the blood inventory in a table
    if inventory:
        st.table(inventory)
    else:
        st.info("No inventory found!")

    # Close the database connection
    cursor.close()
    connection.close()
