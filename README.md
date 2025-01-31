# Failed Snapshot Request Monitor

This Python script monitors a MySQL database for failed snapshot requests and sends email notifications when failures are detected.

## Description

The script connects to a MySQL database, queries for failed snapshot requests within a specified time range (defaulting to the last 24 hours), and sends an email notification if any failed requests are found. It uses a transactional email service (Mailjet in this example) for reliable email delivery.

## Setup

### Prerequisites

*   Python 3.x installed.
*   A MySQL database with the `alice_db.SNAPSHOT_OFFLINE_REQUEST` table.
*   A Mailjet account with API keys.
*   A verified sender email address on Mailjet.

### Installation

1.  Clone the repository:

    ```bash
    git clone [invalid URL removed] # Replace with your repo URL
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
    receiver_emails = email1@example.com, email2@example.com  # Comma-separated list
    ```

    **Important:**
    *   Replace the placeholder values with your actual credentials.
    *   You **must** use a verified sender email address on Mailjet. See the Mailjet documentation below for details on how to verify your sender email.
    *   Receiver emails should be a comma separated list.

### Mailjet Setup and Documentation

1.  **Sign up for a Mailjet account:** If you don't already have one, sign up for a free Mailjet account at [https://www.mailjet.com/](https://www.mailjet.com/).

2.  **Get your API keys:**  In your Mailjet account dashboard, navigate to the API Keys section to obtain your public and private API keys.

3.  **Verify your sender email address:**  You **must** verify the email address you want to use as the "From" address in your emails. This is a crucial step to prevent your emails from being marked as spam.  Follow the instructions in the Mailjet documentation to verify your sender email.

4.  **Mailjet API Documentation:** For more detailed information about the Mailjet API and its features, please refer to the official Mailjet API documentation: [https://dev.mailjet.com/](https://dev.mailjet.com/)

### Running the script

```bash
python get_data.py