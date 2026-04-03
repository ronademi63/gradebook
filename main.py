import argparse
from gradebook import service, storage


def main():
    parser = argparse.ArgumentParser(description="Gradebook Management System")
    subparsers = parser.add_subparsers(
        dest="command", help="Available commands")

    student_parser = subparsers.add_parser("add-student")
    student_parser.add_argument("--name", required=True)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument(
        "type", choices=["students", "courses", "enrollments"])

    gpa_parser = subparsers.add_parser("gpa")
    gpa_parser.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            new_id = service.add_student(args.name)
            print(f"Successfully added {args.name} (ID: {new_id})")

        elif args.command == "list":
            data = storage.load_data()[args.type]
            for item in data:
                print(item)

        elif args.command == "gpa":
            gpa = service.compute_gpa(args.student_id)
            print(f"GPA for Student {args.student_id}: {gpa:.2f}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
