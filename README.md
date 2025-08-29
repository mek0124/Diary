# Diary

A simple CLI diary application built with Python and Click.

## Features

- Add, edit, delete, and list diary entries
- Entries are stored in a JSON file
- Command-line interface

## Requirements

- Python 3.8+
- [Click](https://palletsprojects.com/p/click/)

## Installation

1. Clone the repository:
    ```sh
    git clone <your-repo-url>
    cd Diary
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the CLI:
```sh
python main.py [COMMAND] [OPTIONS]
```

### Commands

- `add` – Add a new diary entry  
  Example:  
  ```sh
  python main.py add --title "My Day" --details "Today was great!"
  ```

- `edit` – Edit an existing entry  
  Example:  
  ```sh
  python main.py edit 1 --title "Updated Title"
  ```

- `delete` – Delete an entry  
  Example:  
  ```sh
  python main.py delete 1
  ```

- `list` – List all entries or a specific entry  
  Example:  
  ```sh
  python main.py list
  python main.py list --entry_id 1
  ```

## Running with Docker

Build the Docker image:
```sh
docker build -t diary-cli .
```

Run the CLI:
```sh
docker run --rm -it -v $(pwd)/data:/app/data diary-cli python main.py [COMMAND] [OPTIONS]
```

## License

MIT