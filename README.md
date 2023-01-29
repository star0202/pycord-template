# Pycord Template by Starcea
## Setup Virtual Environment and Necessary Files
- Make Directory `errors` and `logs`
- Make Empty File `"your database file"` for Database
- Copy `.env.example` to `.env`
    - `.env` file:
        ```py
        TOKEN="your token"
        DATABASE="your database file"
        TEST_GUILD_ID=[test_guild_ids]
        DEV_GUILD_ID=[dev_command_guild_ids]
        ```
- Make Virtual Environment & Activate it
    - POSIX
        ```bash
        $ python3 -m venv venv
        $ . venv/bin/activate
        ```
    - Windows
        ```pwsh
        > python -m venv venv
        > venv/scripts/activate
        ```
- Install Requirements
    ```pwsh
    > pip install -Ur requirements.txt
    ```
## Enjoy Programming!