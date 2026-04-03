Setup and Installation
Project Structure: The project is organized into a main package and several sub-packages to handle data, scripts, and tests.

Virtual Environment: It is recommended to use a virtual environment to manage dependencies.

Create the environment: python -m venv venv

Activate it on Windows/Git Bash: source venv/Scripts/activate

Data Seeding: To populate the system with initial sample data (including Alice Smith and Bob Jones), run the seed script from the root directory.

Command: python -m scripts.seed

CLI Usage
The application uses main.py as the central entry point for all operations, utilizing argparse for command handling.

Add Student: Creates a new record in the gradebook.

python main.py add-student --name "Ron Ademi"

List Students: Displays all current student records.

python main.py list students

Check GPA: Calculates the GPA for a student by computing the simple mean of their course averages.

python main.py gpa --student-id 1

Testing
The project includes unit tests located in tests/test_service.py. These tests utilize the unittest framework and cover student addition, grade entry, and GPA calculations for both happy-path and edge cases.

Run Tests: python -m unittest tests.test_service

Note: When running tests as a module, use dot notation (e.g., tests.test_service) to ensure correct relative imports.

Design Decisions and Limitations
Modular Packaging: Core classes (Student, Course, Enrollment) are implemented in models.py, while persistence is handled separately in storage.py using JSON files.

Input Validation: Small helper functions are utilized to raise ValueErrors for invalid input, such as numeric grades outside the 0–100 range.

Logging: A simple logging mechanism writes INFO and ERROR lines to logs/app.log during data saving/loading or when exceptions occur.

Directory Structure: The main.py file was moved to the project root to ensure proper execution and package discovery during development.

Persistence Limitations: The system uses local JSON storage (data/gradebook.json), which is suitable for local development but not intended for high-concurrency environments.