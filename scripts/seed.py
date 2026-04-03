from gradebook.service import add_student, add_course, enroll, add_grade


def run_seed():
    print("--- Starting Seed Process ---")

    alice_id = add_student("Alice Smith")
    bob_id = add_student("Bob Jones")

    add_course("PY101", "Python Deep Dive")
    add_course("DS202", "Data Structures")

    enroll(alice_id, "PY101")
    add_grade(alice_id, "PY101", 95)

    enroll(bob_id, "DS202")
    add_grade(bob_id, "DS202", 88)

    print(f"Success! Alice (ID: {alice_id}) and Bob (ID: {bob_id}) added.")


if __name__ == "__main__":
    run_seed()
