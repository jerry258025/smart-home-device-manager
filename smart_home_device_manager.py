# Smart Home Device Manager

# Bright Minds Academy

# Dictionary used to store all device information

devices = {}

def add_device():

    # Ask the user for the device name and location

    device_name = input("Enter device name: ").strip()

    location = input("Enter room/location: ").strip()

    # Validation for empty input

    if device_name == "" or location == "":

        print("Device name and location cannot be empty.")

        return

    # Convert name to lowercase for checking duplicates

    device_key = device_name.lower()

    # Check if the device already exists

    if device_key in devices:

        print("This device already exists.")

        return

    # Store the new device

    devices[device_key] = {

        "name": device_name,

        "location": location,

        "status": "Offline"

    }

    print("Device added successfully.")

def update_status():

    # Ask for the device name

    device_name = input("Enter device name: ").strip().lower()

    # Check whether the device exists

    if device_name not in devices:

        print("Device not found.")

        return

    print("\nSelect new status:")

    print("1. Online")

    print("2. Offline")

    print("3. Under Maintenance")

    status_choice = input("Enter choice: ").strip()

    # Validate the status option

    if status_choice == "1":

        new_status = "Online"

    elif status_choice == "2":

        new_status = "Offline"

    elif status_choice == "3":

        new_status = "Under Maintenance"

    else:

        print("Invalid status choice.")

        return

    # Update device status

    devices[device_name]["status"] = new_status

    print("Device status updated successfully.")

def view_devices():

    # Check whether any devices have been added

    if not devices:

        print("No devices have been added.")

        return

    print("\n--- Device List ---")

    # Display every device

    for device in devices.values():

        print("Device:", device["name"])

        print("Location:", device["location"])

        print("Status:", device["status"])

        print("------------------------")

def search_device():

    # Ask for a device name

    device_name = input("Enter device name to search: ").strip().lower()

    # Search for the device

    if device_name in devices:

        device = devices[device_name]

        print("\nDevice found:")

        print("Device:", device["name"])

        print("Location:", device["location"])

        print("Status:", device["status"])

    else:

        print("Device not found.")

def main_menu():

    # Keep displaying the menu until the user exits

    while True:

        print("\n=== Smart Home Device Manager ===")

        print("1. Add New Device")

        print("2. Update Device Status")

        print("3. View Device List")

        print("4. Search for a Device")

        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":

            add_device()

        elif choice == "2":

            update_status()

        elif choice == "3":

            view_devices()

        elif choice == "4":

            search_device()

        elif choice == "5":

            print("Thank you for using the Smart Home Device Manager.")

            break

        else:

            print("Invalid choice. Please enter a number from 1 to 5.")

# Start the program

main_menu()