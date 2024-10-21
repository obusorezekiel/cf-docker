# CloudFormation Template Documentation

![Architectural Diagram](./architectural_diagram.jpeg)

## Overview

This document outlines the implemented CloudFormation template that sets up a web application infrastructure on AWS. The infrastructure includes an EC2 instance running a Docker container, an RDS MySQL database, and an S3 bucket, designed to support a web application.

## Architecture

The implemented architecture consists of the following main components:

1. EC2 Instance: Hosts the web application in a Docker container
2. RDS MySQL Instance: Stores application data
3. S3 Bucket: Used for file storage
4. IAM Role and Instance Profile: Grants necessary permissions to the EC2 instance
5. Security Groups: Control network access to EC2 and RDS instances

## Design Choices

### 1. EC2 Instance

- **Instance Type**: `t2.medium` (default, configurable)
- **AMI**: Amazon Ubuntu (ami-0866a3c8686eaeeba)
- **User Data**: Sets up Docker and runs the application container

**Rationale**: 
- The t2.medium provides a balance of compute and memory resources suitable for a small to medium-sized web application.
- Ubuntu was chosen for its widespread use and compatibility with Docker.
- The User Data script allows for automatic setup and configuration of the instance upon launch.

### 2. RDS Instance

- **Instance Class**: `db.t3.medium` (default, configurable)
- **Engine**: MySQL 8.0.39
- **Storage**: 20 GB (default, configurable)

**Rationale**:
- The db.t3.medium provides sufficient performance for a small to medium-sized database.
- MySQL was chosen for its compatibility with many web applications and its open-source nature.
- 20 GB of storage serves as a starting point and can be increased as needed.

### 3. S3 Bucket

- Created with a dynamic name based on the stack name
- Bucket policy allows the EC2 instance to put objects

**Rationale**:
- S3 provides durable, scalable object storage for application files.
- The dynamic naming ensures uniqueness across different deployments.

### 4. IAM Role and Instance Profile

- Grants EC2 instance permissions to access S3, describe RDS instances, and interact with EC2

**Rationale**:
- This approach follows the principle of least privilege, granting only necessary permissions.
- It allows the EC2 instance to interact with other AWS services securely.

### 5. Security Groups

- EC2 Security Group: Allows inbound traffic on ports 80, 8080, 443, 22, and 3306
- RDS Security Group: Allows inbound traffic on port 3306

**Rationale**:
- This configuration provides necessary access for HTTP, HTTPS, SSH, and database connections while restricting unnecessary access.
- The broad access (0.0.0.0/0) was used for simplicity but should be restricted in a production environment.

## Configuration Steps

1. **Parameter Configuration**:
   - EC2 and RDS instance types were set
   - Database name, username, and password were configured
   - An existing EC2 key pair for SSH access was specified

2. **EC2 Instance Setup**:
   - The User Data script performs the following actions:
     a. Updates the system and installs necessary packages
     b. Installs and configures Docker
     c. Waits for the RDS instance to be available
     d. Pulls and runs the Docker image for the voting application

3. **RDS Instance Setup**:
   - A MySQL database was created with the specified configuration
   - A security group for database access was set up

4. **S3 Bucket Setup**:
   - A bucket was created with a name based on the stack name
   - A bucket policy allowing the EC2 instance to put objects was applied

5. **IAM Role and Instance Profile**:
   - A role with necessary permissions was created
   - The role was attached to an instance profile used by the EC2 instance

6. **Security Group Configuration**:
   - Security groups for EC2 and RDS instances were set up
   - Inbound rules for necessary ports were configured

## Assumptions

1. **Network Configuration**: The template assumes a default VPC is available and does not create new network resources.

2. **Docker Image**: The template assumes the existence of a Docker image (`tony06/voting-app:v1`) containing the voting application.

3. **Database Configuration**: The application is assumed to be compatible with MySQL and capable of using the specified environment variables for database connection.

4. **SSH Access**: The template assumes the user has an existing EC2 key pair for SSH access.

5. **Security**: For simplicity, some security groups allow broad access (0.0.0.0/0). This should be restricted in a production environment.

6. **Scaling**: The template sets up a single EC2 instance and RDS instance. For high availability and scalability, consider using Auto Scaling groups and read replicas.

7. **Region Compatibility**: The AMI ID is region-specific. Ensure it's compatible with your chosen region or use a mapping to provide region-specific AMI IDs.

## Recommendations for Production Use

1. **VPC Configuration**: Set up a custom VPC with public and private subnets for better network isolation.

2. **Security Hardening**: 
   - Restrict security group rules to specific IP ranges or VPC CIDR blocks.
   - Use SSL/TLS for database connections.
   - Implement a bastion host for SSH access.

3. **High Availability**: 
   - Use an Auto Scaling group for EC2 instances.
   - Set up RDS Multi-AZ deployment for database high availability.

4. **Monitoring and Logging**: 
   - Set up CloudWatch alarms for resource utilization.
   - Implement centralized logging using CloudWatch Logs.

5. **Backup and Disaster Recovery**: 
   - Enable automated RDS backups.
   - Implement a disaster recovery strategy, possibly using cross-region replication.

6. **Cost Optimization**: 
   - Use Reserved Instances for predictable workloads.
   - Implement auto-scaling policies based on demand.

7. **Secrets Management**: 
   - Use AWS Secrets Manager or Systems Manager Parameter Store for managing database credentials and other secrets.

By following these recommendations and understanding the design choices and assumptions, this infrastructure can be effectively deployed and managed in both development and production environments.