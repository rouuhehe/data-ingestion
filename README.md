# PetConnect - Cloud Data Analytics Project

## 📋 Overview

PetConnect is a comprehensive cloud-based data analytics project that combines pet adoption management with robust data ingestion, processing, and analytics capabilities. The project demonstrates modern cloud architecture patterns using AWS services, containerized data ingestion, and a modern Angular frontend.

## 🏗️ Architecture

The project consists of four main components the one implemented in this repo is the following:

### 1. **Data Ingestion Service** (`/data-ingestion/`)
- **Purpose**: Automated data extraction from multiple database sources
- **Components**:
  - MySQL ingestion container
  - PostgreSQL ingestion container  
  - MongoDB ingestion container
- **Technology**: Python, Docker, boto3, pandas
- **Output**: CSV/JSON files uploaded to AWS S3

#### Prerequisites
- Node.js 18+ (for frontend)
- Python 3.8+ (for data services)
- Docker & Docker Compose
- AWS CLI configured
- AWS Account with appropriate permissions

## 🛠️ Technical Stack

### Backend
- **Languages**: Python 3.8+
- **Frameworks**: Flask/FastAPI
- **Databases**: MySQL, PostgreSQL, MongoDB
- **Cloud**: AWS (S3, Glue, Athena, EC2)
- **Containerization**: Docker, Docker Compose

### DevOps & Infrastructure
- **Version Control**: Git
- **Cloud Provider**: AWS
- **Container Orchestration**: Docker Compose
- **Data Pipeline**: AWS Glue
- **Analytics**: AWS Athena

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the `data-ingestion/` directory:

```env
# Database Connections
MYSQL_HOST=your-mysql-host
MYSQL_USER=your-mysql-user
MYSQL_PASSWD=your-mysql-password
MYSQL_DB=your-mysql-database

POSTGRES_HOST=your-postgres-host
POSTGRES_USER=your-postgres-user
POSTGRES_PASSWD=your-postgres-password
POSTGRES_DB=your-postgres-database

MONGO_URI=your-mongodb-connection-string

# AWS Configuration
S3_BUCKET=your-s3-bucket-name
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_DEFAULT_REGION=your-aws-region
```

## 🔧 Development

### Running Individual Services

#### Data Ingestion
```bash
cd data-ingestion
docker-compose up ingest_mysql    # MySQL only
docker-compose up ingest_postgres # PostgreSQL only
docker-compose up ingest_mongo    # MongoDB only
```
## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of a cloud computing course and is intended for educational purposes.

## 👥 Team

- **Project Type**: Cloud Data Analytics Platform
- **Course**: Cloud Computing
- **Institution**: UTEC

## 📞 Support

For questions and support, please refer to the individual README files in each service directory or create an issue in the repository.

---

**Built with ❤️ using modern cloud technologies**