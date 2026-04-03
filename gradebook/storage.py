import json
import os
import logging


DEFAULT_PATH = "data/gradebook.json"


def save_data(data, path=DEFAULT_PATH):
    """Saves the global dictionary to a JSON file."""
    try:

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Successfully saved data to {path}")
        logging.info(f"Data saved to {path}")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")
        print(f"Error saving data: {e}")


def load_data(path=DEFAULT_PATH):
    """Loads data from JSON. If file is missing or broken, starts fresh."""
    if not os.path.exists(path):
        logging.info("No storage file found. Starting with empty data.")
        return {"students": [], "courses": [], "enrollments": []}

    try:
        with open(path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logging.error("JSON file is corrupted.")
        print("Warning: Storage file is corrupted. Starting empty.")
        return {"students": [], "courses": [], "enrollments": []}
    except Exception as e:
        logging.error(f"Unexpected error loading data: {e}")
        return {"students": [], "courses": [], "enrollments": []}
