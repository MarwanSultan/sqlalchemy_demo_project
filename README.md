# SQLAlchemy Demo Project

A clean, modular demonstration of SQLAlchemy's ORM and core features, designed for QA engineers and developers to validate and automate database operations. This project showcases best practices in schema design, CRUD operations, transactional integrity, and integration with Python-based test frameworks like pytest. Ideal for learning or extending into real-world data validation and automated QA scenarios.


## Features

- Utilizes SQLAlchemy for ORM-based database interactions.
- Employs Pytest for writing and executing unit tests.
- Includes a sample SQLite database (`test.db`) for testing purposes.
- Structured project layout for scalability and maintainability.

## Project Structure

```bash
sqlalchemy_demo_project/
├── src/
│   ├── config.py
│   ├── main.py
│   ├── models.py
├── tests/
│   ├── conftest.py
│   └── test_sample.py
├── test.db
├── pytest.ini
├── requirements.txt
├── setup.py
└── README.md
```

- `src/`: Contains the main application code, including configuration, entry point, and database models.
- `tests/`: Houses test cases and fixtures for Pytest.
- `test.db`: SQLite database used for testing.
- `pytest.ini`: Configuration file for Pytest.
- `requirements.txt`: Lists project dependencies.
- `setup.py`: Script for installing the package.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MarwanSultan/sqlalchemy_demo_project.git
   cd sqlalchemy_demo_project
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the main application:**

   ```bash
   python src/main.py
   ```

   This will execute the primary functionality defined in `main.py`.

2. **Execute tests using Pytest:**

   ```bash
   pytest
   ```

   This will discover and run all tests located in the `tests/` directory.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
