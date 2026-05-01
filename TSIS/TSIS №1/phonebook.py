import psycopg2
import csv
import json
import os
from config import load_config


def connect():
    config = load_config()
    return psycopg2.connect(**config)


def get_file_path(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, filename)


def import_csv():
    file_path = get_file_path("contacts.csv")

    if not os.path.exists(file_path):
        print("contacts.csv file not found")
        return

    conn = connect()
    cur = conn.cursor()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cur.execute("""
                    INSERT INTO groups(name)
                    VALUES (%s)
                    ON CONFLICT (name) DO NOTHING
                """, (row["group"],))

                cur.execute("""
                    SELECT id FROM groups
                    WHERE name = %s
                """, (row["group"],))

                group_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO contacts(name, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (name)
                    DO UPDATE SET
                        email = EXCLUDED.email,
                        birthday = EXCLUDED.birthday,
                        group_id = EXCLUDED.group_id
                    RETURNING id
                """, (
                    row["name"],
                    row["email"],
                    row["birthday"],
                    group_id
                ))

                contact_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (contact_id, type)
                    DO UPDATE SET phone = EXCLUDED.phone
                """, (
                    contact_id,
                    row["phone"],
                    row["type"]
                ))

        conn.commit()
        print("CSV imported successfully")

    except Exception as e:
        print("Import error:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


def filter_by_group():
    group_name = input("Enter group name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group_name,))

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found")

    cur.close()
    conn.close()


def search_by_email():
    email_part = input("Enter email part: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT name, email
        FROM contacts
        WHERE email ILIKE %s
    """, (f"%{email_part}%",))

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found")

    cur.close()
    conn.close()


def sort_contacts():
    sort_by = input("Sort by (name/birthday/created_at): ")

    allowed = ["name", "birthday", "created_at"]

    if sort_by not in allowed:
        print("Invalid field")
        return

    conn = connect()
    cur = conn.cursor()

    cur.execute(f"""
        SELECT name, email, birthday
        FROM contacts
        ORDER BY {sort_by}
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            c.name,
            c.email,
            c.birthday,
            g.name,
            p.phone,
            p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    rows = cur.fetchall()

    data = []

    for r in rows:
        data.append({
            "name": r[0],
            "email": r[1],
            "birthday": str(r[2]),
            "group": r[3],
            "phone": r[4],
            "type": r[5]
        })

    with open(get_file_path("contacts.json"), "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    cur.close()
    conn.close()

    print("Exported to contacts.json")


def add_contact():   
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    phone = input("Phone: ")
    phone_type = input("Phone type (home/work/mobile): ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO contacts(name, email, birthday)
            VALUES (%s, %s, %s)
            ON CONFLICT (name)
            DO UPDATE SET
                email = EXCLUDED.email,
                birthday = EXCLUDED.birthday
            RETURNING id
        """, (name, email, birthday))

        contact_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES (%s, %s, %s)
            ON CONFLICT (contact_id, type)
            DO UPDATE SET phone = EXCLUDED.phone
        """, (contact_id, phone, phone_type))

        conn.commit()
        print("Contact added successfully")

    except Exception as e:
        print("Error:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()

def move_group():
    name = input("Contact name: ")
    group_name = input("New group: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("""
            CALL move_to_group(%s, %s)
        """, (name, group_name))

        conn.commit()
        print("Moved successfully")

    except Exception as e:
        print("Error:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()


def main():
    while True:
        print("""
1. Import CSV
2. Filter by group
3. Search by email
4. Sort contacts
5. Export JSON
6. Add contact
7. Move to group
0. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            import_csv()

        elif choice == "2":
            filter_by_group()

        elif choice == "3":
            search_by_email()

        elif choice == "4":
            sort_contacts()

        elif choice == "5":
            export_json()

        elif choice == "6":
            add_contact()

        elif choice == "7":
            move_group()

        elif choice == "0":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()