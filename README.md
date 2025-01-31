# Failed Snapshot Request Monitor

This Python script monitors a MySQL database for failed snapshot requests and sends email notifications when failures are detected.

## Description

The script connects to a MySQL database, queries for failed snapshot requests within a specified time range (defaulting to the last 24 hours), and sends an email notification if any failed requests are found.  It uses a transactional email service (Mailjet in this example) for reliable email delivery.

## Setup

### Prerequisites

*   Python 3.x installed.
*   A MySQL database with the `alice_db.SNAPSHOT_OFFLINE_REQUEST` table.
*   A Mailjet account (or another transactional email service with a free tier) with API keys.
*   A verified sender email address on Mailjet.

### Installation

1.  Clone the repository:

    ```bash
    git clone [invalid URL removed]  # Replace with your repo URL
    cd failed-snapshot-request-monitor
    ```

2.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  Create a `config.ini` file in the project directory.

2.  Populate the `config.ini` file with your database and email settings:

    ```ini
    [database]
    username = your_db_username
    password = your_db_password
    host = your_db_host
    port = 3306  # Default MySQL port
    database = alice_db

    [email]
    mailjet_api_key_public = YOUR_MAILJET_PUBLIC_KEY
    mailjet_api_key_private = YOUR_MAILJET_PRIVATE_KEY
    sender_email = your_verified_mailjet_sender_email  # Must be verified on Mailjet
    receiver_email = your_email@example.com
    ```

    **Important:**
    *   Replace the placeholder values with your actual credentials.
    *   For Gmail (if you choose to use it temporarily for testing), create an "App Password" in your Gmail account settings and use that as the `sender_password`.  Do *not* use your regular Gmail password.
    *   For production, it's even better to store the email password as an environment variable and retrieve it in your script using `os.environ.get("EMAIL_PASSWORD")`.

### Running the script

```bash
python get_data.py
