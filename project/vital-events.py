import os

DATA_FILE = "vital_records.txt"


# -----------------------------
# Utility Functions
# -----------------------------

def load_records():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def save_records(records):
    with open(DATA_FILE, "w") as f:
        for r in records:
            f.write(r + "\n")


def generate_next_code(records):
    if not records:
        return "1"
    last = records[-1]
    code = int(last.split(":")[0])
    return str(code + 1)


def is_valid_date(date):
    if len(date) != 10:
        return False
    if date[4] != "-" or date[7] != "-":
        return False
    try:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
    except:
        return False

    return (1900 <= year <= 2100) and (1 <= month <= 12) and (1 <= day <= 31)


def is_valid_gender(gender):
    return gender.upper() in ["M", "F"]


def find_record_by_code(records, code):
    for i, record in enumerate(records):
        if record.split(":")[0] == code:
            return i
    return -1


def parse_record(record):
    first = record.find(":")
    second = record.find(":", first + 1)

    code = record[:first]
    record_type = record[first + 1:second]

    details = record[second + 2:]
    attributes = [item.strip() for item in details.split(",")]

    return code, record_type, attributes


# -----------------------------
# Features
# -----------------------------

def register_record(records, record_type):
    code = generate_next_code(records)
    attributes = []

    print("\n╭─────────────────────────╮")
    print(f"│   {record_type} REGISTRATION")
    print("├─────────────────────────┤")

    if record_type == "Birth":
        child = input("│ Child's Full Name: ")
        mother = input("│ Mother's Full Name: ")
        gender = ""

        while True:
            gender = input("│ Gender (M/F): ")
            if is_valid_gender(gender):
                break
            print("│ ⚠️ Invalid gender. Enter M or F.")

        date = ""
        while True:
            date = input("│ Date (YYYY-MM-DD): ")
            if is_valid_date(date):
                break
            print("│ ⚠️ Invalid date format.")

        attributes = [child, mother, gender, date]

    elif record_type == "Marriage":
        s1 = input("│ Spouse 1 Full Name: ")
        s2 = input("│ Spouse 2 Full Name: ")

        date = ""
        while True:
            date = input("│ Date (YYYY-MM-DD): ")
            if is_valid_date(date):
                break
            print("│ ⚠️ Invalid date format.")

        location = input("│ Location: ")
        attributes = [s1, s2, date, location]

    elif record_type == "Divorce":
        p1 = input("│ Person 1 Full Name: ")
        p2 = input("│ Person 2 Full Name: ")
        date = input("│ Date of Divorce (YYYY-MM-DD): ")
        reason = input("│ Reason: ")

        attributes = [p1, p2, date, reason]

    print("╰─────────────────────────╯")

    rec_str = f"{code}:{record_type}: " + ", ".join(attributes)
    records.append(rec_str)
    save_records(records)

    print("\n┌─ Record Added ─┐")
    print(f"│ ✓ {record_type} registration complete.")
    print(f"│ ✓ Record Code: {code}")
    print("└───────────────┘")


def display_all_records(records):
    print("\n╭───────────────────────────────────────────────────────╮")
    print("│                    ALL RECORDS                        │")
    print("├───────────────────────────────────────────────────────┤")

    if not records:
        print("│ No records found.")
    else:
        for r in records:
            print("│", r)

    print("╰───────────────────────────────────────────────────────╯")


def delete_record(records):
    print("\n╭─────────────────────────╮")
    print("│   DELETE RECORD         │")
    print("├─────────────────────────┤")

    code = input("│ Enter Record Code: ")
    print("╰─────────────────────────╯")

    index = find_record_by_code(records, code)

    if index == -1:
        print("┌─ Error ─┐")
        print("│ No record found with code:", code)
        print("└─────────┘")
        return

    print("┌─ Confirm Deletion ─┐")
    print("│ Record found:", records[index])
    confirm = input("│ Delete this record? (y/n): ")

    if confirm.lower() == "y":
        del records[index]
        save_records(records)
        print(f"│ ✓ Record {code} deleted successfully")
    else:
        print("│ Deletion cancelled")

    print("└───────────────┘")


def search_by_name(records):
    print("\n╭─────────────────────────╮")
    print("│   SEARCH BY NAME        │")
    print("├─────────────────────────┤")
    name = input("│ Enter Name to Search: ")
    print("╰─────────────────────────╯")

    matches = [r for r in records if name.lower() in r.lower()]

    print("\n╭───────────────────────────────────────────────────────╮")
    print("│                  SEARCH RESULTS                       │")
    print("├───────────────────────────────────────────────────────┤")

    if not matches:
        print(f"│ No records found matching '{name}'")
    else:
        print(f"│ Found {len(matches)} matching record(s):")
        for i, m in enumerate(matches, 1):
            print(f"│ {i}. {m}")

    print("╰───────────────────────────────────────────────────────╯")


def generate_certificate(record):
    code, record_type, attributes = parse_record(record)

    print("\n╭────────────────────────────────────────────╮")
    print("│         CERTIFICATE OF REGISTRATION        │")
    print("├────────────────────────────────────────────┤")
    print("│ This certifies that the information below")
    print("│ is a true and accurate record.")
    print("├────────────────────────────────────────────┤")
    print("│ Registration Number:", code)
    print("│ Document Type:", record_type)

    if record_type == "Birth":
        print("│ Child's Full Name:", attributes[0])
        print("│ Mother's Full Name:", attributes[1])
        print("│ Date of Birth:", attributes[3])
        print("│ Gender:", attributes[2])

    elif record_type == "Marriage":
        print("│ Spouse 1 Full Name:", attributes[0])
        print("│ Spouse 2 Full Name:", attributes[1])
        print("│ Date of Marriage:", attributes[2])
        print("│ Location:", attributes[3])

    elif record_type == "Divorce":
        print("│ Person 1 Full Name:", attributes[0])
        print("│ Person 2 Full Name:", attributes[1])
        print("│ Date of Divorce:", attributes[2])
        print("│ Reason:", attributes[3])

    print("╰────────────────────────────────────────────╯")


# -----------------------------
# Main Program
# -----------------------------

def main():
    print("┌──────────────────┐")
    records = load_records()
    if records:
        print("│ ✓ Records loaded")
    else:
        print("│ ℹ No existing records found")
    print("└──────────────────┘")

    while True:
        print("\n╭──────────────────────────────────────╮")
        print("│    VITAL EVENT REGISTRATION SYSTEM   │")
        print("├──────────────────────────────────────┤")
        print("│ 1. Birth Registration")
        print("│ 2. Marriage Registration")
        print("│ 3. Divorce Registration")
        print("│ 4. Display All Records")
        print("│ 5. Generate Certificate")
        print("│ 6. Delete Record by Code")
        print("│ 7. Search Records by Name")
        print("│ 8. Exit")
        print("╰──────────────────────────────────────╯")

        choice = input("Enter choice [1-8]: ")

        if choice == "1":
            register_record(records, "Birth")
        elif choice == "2":
            register_record(records, "Marriage")
        elif choice == "3":
            register_record(records, "Divorce")
        elif choice == "4":
            display_all_records(records)
        elif choice == "5":
            code = input("\n┌─ Certificate Generation ─┐\n│ Enter record code: ")
            index = find_record_by_code(records, code)
            if index != -1:
                generate_certificate(records[index])
            else:
                print("│ ⚠️ Error: Record not found:", code)
            print("└─────────────────────────┘")
        elif choice == "6":
            delete_record(records)
        elif choice == "7":
            search_by_name(records)
        elif choice == "8":
            print("\n┌─ Exiting System ─┐")
            print("│ ℹ All records saved")
            print("└─────────────────┘")
            break
        else:
            print("\n┌─ Error ─┐")
            print("│ ⚠️ Invalid choice! Enter 1-8.")
            print("└─────────┘")

        cont = input("\nContinue? [y/n]: ")
        if cont.lower() != "y":
            break

    print("\n╭──────────────────────────╮")
    print("│    SYSTEM TERMINATED     │")
    print("╰──────────────────────────╯")


if __name__ == "__main__":
    main()
