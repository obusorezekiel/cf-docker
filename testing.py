import boto3
import pymysql
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# RDS connection settings
rds_endpoint = "<your RDS instance Endpoint"  # Replace with your RDS endpoint
db_name = "<your_dbname>"
db_username = "your db_user"
db_password = "your db_pass"  # Store securely in production
db_port = 3306

# S3 settings
bucket_name = "my-app-stack-s3-bucket"
file_name = "test_file.txt"
file_content = "This is a test file to upload to S3."

# Function to test RDS connection


def test_rds_connection():
    try:
        # Connect to the RDS MySQL database
        connection = pymysql.connect(
            host=rds_endpoint,
            user=db_username,
            password=db_password,
            database=db_name,
            port=db_port
        )
        print("Connected to RDS MySQL database.")

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS my_database;")

        # Switch to the database
        cursor.execute("USE my_database;")

        # Create the table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                position VARCHAR(255) NOT NULL,
                salary DECIMAL(10, 2)
            );
        """)

        # Insert values into the table
        cursor.execute("""
        INSERT INTO employees (name, position, salary)
        VALUES 
            ('John Doe', 'Manager', 75000),
            ('Jane Smith', 'Developer', 65000),
            ('Emily Johnson', 'Designer', 55000);
        """)

        # Commit the transaction
        connection.commit()

        print("Database and table created, and values inserted successfully.")

        # Close the connection
        connection.close()
        print("Connection to RDS closed.")
    except Exception as e:
        print(f"Error connecting to RDS: {e}")

# Function to test S3 file upload


def test_s3_upload():
    try:
        # Initialize a session using Amazon S3
        s3 = boto3.client('s3')

        # Create a file to upload
        with open(file_name, 'w') as file:
            file.write(file_content)

        # Upload the file to S3
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"File '{file_name}' uploaded to S3 bucket '{bucket_name}'.")

        # Cleanup: delete the local file
        os.remove(file_name)
    except (NoCredentialsError, PartialCredentialsError) as e:
        print("Credentials not available for S3 access:", e)
    except Exception as e:
        print(f"Error uploading file to S3: {e}")


if __name__ == "__main__":
    # Test RDS connection
    test_rds_connection()

    # Test S3 file upload
    test_s3_upload()
