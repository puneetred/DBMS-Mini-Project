import streamlit as st
import mysql.connector

def find_donors_page():
    st.subheader("Find Donors")

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="blood_bank_management"
    )
    cursor = connection.cursor()

    # Find donors form
    with st.form("find_donors_form"):
        st.write("Enter recipient requirements:")
        blood_group = st.selectbox("Required Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])

        # Add more recipient requirements as needed
        submit_button = st.form_submit_button("Find Donors")

    # Handle form submission
    if submit_button:
        # Prepare the SQL query and parameter values based on the selected filters
        query = "SELECT * FROM donors WHERE blood_group = %s"
        values = (blood_group,)

        # Retrieve donors matching the recipient requirements from the database
        cursor.execute(query, values)
        donors = cursor.fetchall()

        # Display the inventory summary
        inventory_query = "SELECT blood_group, SUM(quantity) FROM blood_inventory GROUP BY blood_group"
        cursor.execute(inventory_query)
        inventory_summary = cursor.fetchall()

        if inventory_summary:
            st.subheader("Inventory Summary")
            for group, quantity in inventory_summary:
                st.write(f"{group}: {quantity}")
            st.write("---")

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
