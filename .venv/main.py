import streamlit as st
import add_donor
import retrieve_donors
import retrieve_recipients
import find_donors
import add_donations
import blood_inventory
import make_transfusion

def main():
    st.title("Blood Bank Management System")

    # Sidebar menu options
    menu_options = ["Add Donor", "Find Donor", "Retrieve All Donors", "Retrieve All Recipients", "Add Donation", "Make Transfusion", "Blood Inventory"]
    selected_option = st.sidebar.selectbox("Select an option", menu_options)

    # Execute respective functions based on the selected option
    if selected_option == "Add Donor":
        add_donor.add_donor_page()
    elif selected_option == "Find Donor":
        find_donors.find_donors_page()
    elif selected_option == "Retrieve All Donors":
        retrieve_donors.retrieve_donors_page()
    elif selected_option == "Retrieve All Recipients":
        retrieve_recipients.retrieve_recipients_page()
    elif selected_option == "Add Donation":
        add_donations.add_donation_page()
    elif selected_option == "Blood Inventory":
        blood_inventory.inventory_page()
    elif selected_option == "Make Transfusion":
        make_transfusion.make_transfusion_page()

if __name__ == "__main__":
    main()
