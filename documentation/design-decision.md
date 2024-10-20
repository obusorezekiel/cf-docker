# Design Decisions Documentation

## 1. Infrastructure as Code (IaC)
**Decision**: Used AWS CloudFormation for infrastructure provisioning.
**Rationale**: 
- Ensures reproducibility and consistency across environments.
- Allows version control of infrastructure.
- Simplifies updates and rollbacks.

## 2. Compute: EC2 Instance
**Decision**: Used a single EC2 instance to host the application.
**Rationale**:
- Simplifies initial setup and management.
- Suitable for development and testing environments.
- Allows easy SSH access for troubleshooting.

## 3. Containerization: Docker
**Decision**: Deploy the application using Docker.
**Rationale**:
- Ensures consistency across different environments.
- Simplifies deployment and updates.
- Allows for easy scaling and portability.

## 4. Database: Amazon RDS for MySQL
**Decision**: Use Amazon RDS for the database instead of a self-managed database on EC2.
**Rationale**:
- Reduces administrative overhead (backups, patching, etc.).
- Provides easy scalability and high availability options.
- Offers better security and compliance features.

## 5. Storage: Amazon S3
**Decision**: Include an S3 bucket for object storage.
**Rationale**:
- Provides durable and scalable storage for application assets or user uploads.
- Can be used for backups or static website hosting if needed.

## 6. Security: IAM Roles and Security Groups
**Decision**: Use IAM roles for EC2 and separate security groups for EC2 and RDS.
**Rationale**:
- Follows the principle of least privilege.
- Allows fine-grained control over resource access.
- Improves security by eliminating the need for hardcoded credentials.

## 7. Configuration: Parameterization
**Decision**: Use CloudFormation parameters for key configuration items.
**Rationale**:
- Allows flexibility in deployment without changing the template.
- Supports different environments (dev, staging, prod) with the same template.

## 8. Application Deployment: User Data Script
**Decision**: Use EC2 User Data for initial application setup and deployment.
**Rationale**:
- Automates the initial setup process.
- Ensures the application is ready to use immediately after instance launch.

## 9. Network Access: Open Access
**Decision**: Allow broad network access in security groups.
**Rationale**:
- Simplifies initial setup and testing.
**Considerations**:
- Not suitable for production environments.
- Should be restricted to specific IP ranges or VPC for better security.

## 10. Database Access: Direct from EC2
**Decision**: Allow direct access to RDS from EC2 instance.
**Rationale**:
- Simplifies the initial architecture.
**Considerations**:
- For production, consider using a bastion host or VPN for database access.

These design decisions create a functional and relatively simple architecture suitable for development and testing purposes. However, several enhancements would be necessary for a production-grade deployment, particularly in the areas of scalability, high availability, and security.