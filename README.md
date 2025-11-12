# WebApp with Redis on AWS 🚀

This project demonstrates a full-stack web application integrated with **Redis** for fast in-memory data storage, deployed initially locally and later on AWS. The application allows users to browse products and manage a shopping cart, leveraging Redis for quick and efficient data access.

---

## Overview

The project is divided into three phases:

1. **Phase 0 – Local Setup** 🛠️  
   - A local development environment was created using **Docker** for both Redis and Flask.  
   - Redis runs in a dedicated container (`redis-local`) and Flask in another (`webapp-local`).  
   - The script `initialize_redis.py` loads a predefined set of 10 products into Redis for testing.  
   - This phase allows validation of Redis functionality and product initialization without consuming AWS resources.

2. **Phase 1 – AWS ElastiCache Integration** ☁️  
   - Redis was migrated to **AWS ElastiCache (Redis OSS)**.  
   - `initialize_redis.py` was configured to connect to the cloud Redis instance to populate product data.  
   - The application was adapted to connect to the ElastiCache endpoint.  
   - SSL connections were optionally enabled for secure communication.

3. **Phase 2 – Web Application Deployment** 🌐  
   - The Flask web application was deployed to an **EC2 instance**.  
   - Users can view the list of products, add them to a shopping cart, and complete a checkout process.  
   - The shopping cart data is stored in Redis, ensuring low-latency access and real-time updates.  
   - The application is accessible via the EC2 public IP, while Redis remains accessible only from within the VPC or container network for security.

---

## Features

- Fast in-memory product database using Redis  
- Modular Docker setup for local development  
- Flask web application with shopping cart functionality  
- Secure AWS deployment using ElastiCache and EC2  
- Easy scalability and cloud readiness  

---

## Local Setup

1. Build and start containers:

```bash
docker compose up --build -d
````

2. Initialize Redis with products:

```bash
docker exec -it webapp-local python initialize_redis.py
```

3. Verify products in Redis:

```bash
docker exec -it redis-local redis-cli
127.0.0.1:6379> keys *
```

---

## AWS Deployment Notes

* Redis is hosted on **AWS ElastiCache (Redis OSS)**.
* Flask app runs on an **EC2 instance**, connected to Redis securely.
* Docker can be optionally used on EC2 for consistent deployment.
* Security Groups ensure:

  * SSH access restricted to the administrator’s IP.
  * HTTP/HTTPS accessible publicly.
  * Redis access restricted to application instances only.

---

## Dependencies

* Docker & Docker Compose
* Python 3.9+
* Flask
* redis-py library
