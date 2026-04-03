from connect import get_connection


def insert_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    conn.close()
    print("Contact added/updated successfully.")


def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    
    if rows:
        for row in rows:
            print(f"Name: {row[0]}, Phone: {row[1]}")
    else:
        print("No contacts found.")

    conn.close()


def search_contacts():
    conn = get_connection()
    cur = conn.cursor()

    pattern = input("Search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(f"Name: {row[0]}, Phone: {row[1]}")
    else:
        print("No matching contacts found.")

    conn.close()


def delete_contact():
    conn = get_connection()
    cur = conn.cursor()

    value = input("Enter name or phone to delete: ")

    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    conn.close()
    print("Contact deleted successfully.")


def bulk_insert():
    conn = get_connection()
    cur = conn.cursor()

    names = ["Zhansaya", "Zhiger", "Thor", "Bibiziyana"]
    phones = ["87001234567", "87005554433", "87009998877", "87777777777"]

    cur.execute("CALL insert_many_contacts(%s, %s)", (names, phones))
    conn.commit()
    conn.close()
    print("Bulk insert completed 100%!")


def menu():
    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1 - Add/Update contact")
        print("2 - Show contacts (pagination)")
        print("3 - Search contacts")
        print("4 - Delete contact")
        print("5 - Bulk insert")
        print("0 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            bulk_insert()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("ERROOOR!")

if __name__ == "__main__":
    menu()