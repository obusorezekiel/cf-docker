# Architecture Documentation

## Overview
This CloudFormation template defines a web application infrastructure on AWS, consisting of an EC2 instance, an RDS MySQL database, and an S3 bucket. The architecture is designed to host a web application containerized with Docker with access to the RDS instance from the container.

## Components

### 1. EC2 Instance (WebAppEC2Instance)
- **Purpose**: Hosts the Docker container running the web application.
- **Instance Type**: Configurable, default is t2.medium.
- **AMI**: Amazon Ubuntu (ami-0866a3c8686eaeeba).
- **Key Pair**: Uses a user-specified EC2 KeyPair for SSH access.

### 2. RDS MySQL Instance (MyRDSInstance)
- **Purpose**: Stores application data.
- **Instance Class**: Configurable, default is db.t3.medium.
- **Engine**: MySQL 8.0.39.
- **Storage**: Configurable, default is 20GB.

### 3. S3 Bucket (S3Bucket)
- **Purpose**: Object storage for the application (e.g., file uploads, backups).
- **Naming**: Uses the stack name as a prefix for uniqueness.

### 4. Security Groups
- **EC2 Security Group (EC2SecurityGroup)**: Controls inbound traffic to the EC2 instance.
- **RDS Security Group (RDSDBSecurityGroup)**: Controls inbound traffic to the RDS instance.

### 5. IAM Role and Instance Profile
- **EC2 Role (EC2Role)**: Defines permissions for the EC2 instance.
- **Instance Profile (EC2InstanceProfile)**: Attaches the IAM role to the EC2 instance.

## Network Flow
1. Users access the application via HTTP (80), HTTPS (443), or a custom port (8080) on the EC2 instance.
2. The EC2 instance communicates with the RDS database on port 3306.
3. The EC2 instance can interact with the S3 bucket for object storage.

## Application Deployment
- The web application is containerized and pulled from a Docker Hub repository (tony06/voting-app:v1).
- Docker and Docker Compose are installed on the EC2 instance during initialization.
- The application container is configured with environment variables to connect to the RDS database.

## Scalability and High Availability
- The current architecture is single-instance and not inherently highly available.
- Scalability can be achieved by adjusting the EC2 and RDS instance types.
- For improved availability and scalability, consider:
  - Using an Auto Scaling Group for EC2 instances.
  - Implementing a load balancer (e.g., Application Load Balancer).
  - Utilizing RDS Multi-AZ deployment.

## Monitoring and Logging
- While not explicitly defined in the template, AWS CloudWatch can be used for monitoring EC2 and RDS metrics.
- Consider implementing custom CloudWatch Logs for application-specific logging.

This architecture provides a basic setup for a web application with a database backend and object storage. It's suitable for development and testing environments.