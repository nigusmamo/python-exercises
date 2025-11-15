import time
import os

class Contact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.next = None

head = None


# ======================= FILE HANDLING =======================

def load_from_file():
    global head
    if not os.path.exists("contacts.txt"):
        print("contacts.txt not found. Starting with an empty list.")
        return

    head = None
    tail = None

    with open("contacts.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            fname, lname, phone, email = parts
            new_contact = Contact(fname, lname, phone, email)

            if head is None:
                head = new_contact
                tail = new_contact
            else:
                tail.next = new_contact
                tail = new_contact

    print("Contacts loaded from file.")


def save_to_file():
    global head
    with open("contacts.txt", "w") as file:
        temp = head
        while temp:
            file.write(f"{temp.first_name},{temp.last_name},{temp.phone},{temp.email}\n")
            temp = temp.next


# ======================= UTILITIES =======================

def is_duplicate(phone):
    temp = head
    while temp:
        if temp.phone == phone:
            return True
        temp = temp.next
    return False


def get_contact_data():
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name (optional): ")
    phone = input("Enter Phone Number: ")

    if is_duplicate(phone):
        print("A contact with this phone number already exists.")
        return None

    email = input("Enter Email (optional): ")
    return Contact(fname, lname, phone, email)


# ======================= ADD CONTACT =======================

def add_contact_beginning():
    global head
    new_contact = get_contact_data()
    if not new_contact:
        return

    new_contact.next = head
    head = new_contact
    print("Contact added at the beginning!")
    save_to_file()


def add_contact_end():
    global head
    new_contact = get_contact_data()
    if not new_contact:
        return

    if head is None:
        head = new_contact
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_contact

    print("Contact added at the end!")
    save_to_file()


def add_contact_position():
    global head

    if head is None:
        print("List empty. Adding at beginning.")
        add_contact_beginning()
        return

    # count nodes
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next

    pos = int(input(f"Enter position (1 to {count+1}): "))

    if pos < 1 or pos > count + 1:
        print("Invalid position!")
        return

    if pos == 1:
        add_contact_beginning()
        return
    if pos == count + 1:
        add_contact_end()
        return

    new_contact = get_contact_data()
    if not new_contact:
        return

    temp = head
    for _ in range(pos - 2):
        temp = temp.next

    new_contact.next = temp.next
    temp.next = new_contact

    print(f"Contact added at position {pos}!")
    save_to_file()


def add_contact():
    print("\nWhere do you want to add the contact?")
    print("1. At Beginning")
    print("2. At End")
    print("3. At Position")
    ch = int(input("Choice: "))

    if ch == 1:
        add_contact_beginning()
    elif ch == 2:
        add_contact_end()
    elif ch == 3:
        add_contact_position()
    else:
        print("Invalid choice!")


# ======================= DELETE =======================

def delete_contact():
    global head
    phone = input("Enter phone number to delete: ")

    temp = head
    prev = None

    while temp and temp.phone != phone:
        prev = temp
        temp = temp.next

    if not temp:
        print("Contact not found!")
        return

    if not prev:
        head = temp.next
    else:
        prev.next = temp.next

    print("Contact deleted!")
    save_to_file()


# ======================= VIEW =======================

def view_contacts():
    global head
    if head is None:
        print("\nNo contacts available.")
        return

    print("\n--- All Contacts ---")
    temp = head
    while temp:
        print(f"Name: {temp.first_name} {temp.last_name}")
        print(f"Phone: {temp.phone}")
        print(f"Email: {temp.email}")
        print("------------------")
        temp = temp.next


# ======================= SEARCH =======================

def search_contact():
    global head
    keyword = input("Enter name or phone to search: ")

    temp = head
    while temp:
        if temp.first_name == keyword or temp.last_name == keyword or temp.phone == keyword:
            print("\n--- Contact Found ---")
            print(f"Name: {temp.first_name} {temp.last_name}")
            print(f"Phone: {temp.phone}")
            print(f"Email: {temp.email}")
            return
        temp = temp.next

    print("Contact not found!")


# ======================= SORTING =======================

def compare(a, b):
    return (a.first_name + a.last_name) > (b.first_name + b.last_name)


def swap(a, b):
    a.first_name, b.first_name = b.first_name, a.first_name
    a.last_name, b.last_name = b.last_name, a.last_name
    a.phone, b.phone = b.phone, a.phone
    a.email, b.email = b.email, a.email


def bubble_sort():
    global head
    if not head or not head.next:
        return

    swapped = True
    last_sorted = None

    while swapped:
        swapped = False
        current = head
        while current.next != last_sorted:
            if compare(current, current.next):
                swap(current, current.next)
                swapped = True
            current = current.next
        last_sorted = current

    print("Contacts sorted using Bubble Sort!")


def insertion_sort():
    global head
    if not head or not head.next:
        return

    sorted_list = None
    current = head

    while current:
        next_node = current.next
        current.next = None

        if not sorted_list or compare(sorted_list, current):
            current.next = sorted_list
            sorted_list = current
        else:
            search = sorted_list
            while search.next and not compare(current, search.next):
                search = search.next

            current.next = search.next
            search.next = current

        current = next_node

    head = sorted_list
    print("Contacts sorted using Insertion Sort!")


def selection_sort():
    global head
    if not head or not head.next:
        return

    i = head
    while i:
        min_node = i
        j = i.next
        while j:
            if compare(min_node, j):
                min_node = j
            j = j.next

        if min_node != i:
            swap(min_node, i)

        i = i.next

    print("Contacts sorted using Selection Sort!")


def sort_menu():
    print("\nChoose sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")

    ch = int(input("Choice: "))

    start = time.time()

    if ch == 1:
        bubble_sort()
    elif ch == 2:
        insertion_sort()
    elif ch == 3:
        selection_sort()
    else:
        print("Invalid choice!")
        return

    duration = (time.time() - start) * 1_000_000
    print(f"Sorted in {int(duration)} microseconds")

    save_to_file()


# ======================= MENU =======================

def menu():
    print("\n==== Contact Management System ====")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Sort Contacts")
    print("5. View All Contacts")
    print("6. Exit")
    return int(input("Enter choice: "))


# ======================= MAIN =======================

def main():
    load_from_file()

    while True:
        choice = menu()
        if choice == 1:
            add_contact()
        elif choice == 2:
            delete_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            sort_menu()
        elif choice == 5:
            view_contacts()
        elif choice == 6:
            save_to_file()
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
