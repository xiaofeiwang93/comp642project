import csv

# File path for the CSV database
csv_file = "data.csv"

# Function to create the initial CSV file
def create_csv_file():
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age"])

def get_next_id(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            existing_ids = [int(row['ID']) for row in reader]

        return max(existing_ids) + 1
    except FileNotFoundError:
        return 1  # If the file doesn't exist, start with 1 as the first ID

def add_record(filename, record):
    next_id = get_next_id(filename)
    record['ID'] = next_id

    with open(filename, 'a', newline='') as file:
        fieldnames = record.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:  # If the file is empty, write the header row
            writer.writeheader()

        writer.writerow(record)

# Function to add a new record to the CSV
def add_record(record):
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)

# Function to read all records from the CSV
def read_all_records():
    records = []
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
    return records

# Function to search for a record by ID
def search_record_by_id(search_id):
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] == search_id:
                return row
    return None

# Function to update a record by ID
def update_record_by_id(update_id, new_data):
    records = read_all_records()
    for record in records:
        if record["ID"] == update_id:
            record.update(new_data)
            break

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Age"])
        writer.writeheader()
        for record in records:
            writer.writerow(record)

# Usage example
if __name__ == "__main__":
    # Create the CSV file if it doesn't exist
    create_csv_file()

    # Add a new record
    new_record = ["001", "Alice", "30"]
    add_record(new_record)

    # Read all records
    all_records = read_all_records()
    print("All Records:")
    for record in all_records:
        print(record)

    # Search for a record by ID
    search_id = "001"
    found_record = search_record_by_id(search_id)
    print(f"Record with ID {search_id}: {found_record}")

    # Update a record
    update_id = "001"
    updated_data = {"Name": "Alicia", "Age": "31"}
    update_record_by_id(update_id, updated_data)
    print("Updated Record:")
    print(search_record_by_id(update_id))