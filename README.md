# ✈️ Airline Data System — Hive + Hadoop + PostgreSQL

A containerized data infrastructure for analyzing flight delay datasets using Hive, HDFS, Spark, and PostgreSQL — powered by DBeaver for SQL querying and backed by pre-commit hooks for robust dev hygiene.

## 📖 Overview
This project sets up a data processing stack using Apache Hive on Hadoop with PostgreSQL as the metastore. It allows you to query flight delay data stored in HDFS using SQL, with DBeaver as the UI for easy interaction.
The stack includes HiveServer2 for SQL queries, a Hadoop cluster for distributed storage, and PostgreSQL for metadata management. The setup is designed to be easily deployable using Docker Compose.

## Sources

| Source                                                                                                                                          | Purpose                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| OpenSky Network <br/>Aviationstack<br/>FlightAware<br/>Bureau of Transportation Statistics (BTS)<br/>Amadeus SDK (if available)<br/>FlightRadar | Historical flight data and statistics |
| OpenSky API, ADS-B Exchange                                                                                                                     | Real time flight data                 |
| Kaggle Datasets                                                                                                                                 | Sample datasets for testing           |
| OpenWeather                                                                                                                                     | Weather API                           |
| Google<br/>TripAdvisor<br/>Public APIs                                                                                                          | Web scraping for sentiment analysis   |

## 📦 Stack Overview

| Service          | Purpose                                 |
|------------------|-----------------------------------------|
| HiveServer2      | SQL engine to query data in HDFS        |
| Hive Metastore   | Stores Hive metadata in PostgreSQL      |
| Hadoop           | HDFS Namenode + Datanode                |
| PostgreSQL       | Hive metastore backend                  |
| Spark (optional) | Distributed processing engine           |
| Adminer/DBeaver  | UI for querying and managing PostgreSQL |

---

## 🚀 Setup Instructions

### Clone & Configure

```bash
git clone https://github.com/anderdam/airline-data-system.git
cd airline-data-system
```

Make sure the following are included:
- docker-compose.yml
- hive-site.xml
- .gitignore
- .pre-commit-config.yaml
- .secrets.baseline (optional)
- README.md

### Start Services
```bash
docker-compose down -v
docker-compose up -d
```

### Format HDFS (First-Time Only)
```bash
docker exec -it hadoop-namenode hdfs namenode -format
docker-compose restart hadoop-namenode hadoop-datanode
```

### 🛠 Hive Metastore Initialization

Ensure PostgreSQL is using MD5 authentication:
- Inside Postgres container, edit:
  - /var/lib/postgresql/data/pg_hba.conf → host all all 0.0.0.0/0 md5
  - /var/lib/postgresql/data/postgresql.conf → password_encryption = md5

- Reload configs:
    ```sql
    SELECT pg_reload_conf();
    ALTER ROLE "user" WITH PASSWORD 'password';
    ```

Then initialize Hive schema:
```bash
docker exec -it hive-server bash
schematool -dbType postgres -initSchema --verbose
```

### 📁 hive-site.xml Configuration
Mounted at /opt/hive/conf/hive-site.xml with key properties:
```xml
<property>
  <name>javax.jdo.option.ConnectionURL</name>
  <value>jdbc:postgresql://postgres-db:5432/flights</value>
</property>
<property>
  <name>hive.metastore.schema.verification</name>
  <value>false</value>
</property>
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://hadoop-namenode:8020</value>
</property>
```

Expose HiveServer2 on port 10001 for DBeaver connection:
```
jdbc:hive2://localhost:10001/default
```


🗃️ Sample Hive Table
```sql
CREATE TABLE flights (
  flight_date STRING,
  airline_code STRING,
  flight_number STRING,
  origin STRING,
  destination STRING,
  departure_delay INT,
  arrival_delay INT,
  cancelled BOOLEAN,
  diverted BOOLEAN
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

Load data from HDFS:
```sql
LOAD DATA INPATH '/user/hive/warehouse/flights/flights.csv' INTO TABLE flights;
```

### 🧼 Dev Hygiene
📄 .gitignore Includes:
- Docker logs, temp files, system junk
- Hive runtime artifacts (derby.log, metastore_db)
- IDE configs (.vscode/, .idea/)
- Secrets (.env, .dbeaver-data-sources.json)

🛡️ .pre-commit-config.yaml Hooks:
- black for Python formatting
- isort for import cleanup
- YAML linting
- Trailing whitespace fixer
- Secret scanning via detect-secrets

Generate secret baseline:
```
detect-secrets scan > .secrets.baseline
```

Enable hooks:
```
pre-commit install
pre-commit run --all-files
```


🧠 Troubleshooting Tips


| Problem         | Solution                                            |
|-----------------|-----------------------------------------------------|
| HiveServer2 not listening on port   | Recheck schema initialization and metastore config |
| SCRAM-SHA-256 error from Postgres | Switch to MD5 in pg_hba.conf and postgresql.conf |
| ALTER ROLE syntax error | Use double quotes: ALTER ROLE "user" |
| .git push fails with refspec error | Ensure branch and first commit exist |


## 🛠️ Development Environment

### Local Development
For local development, ensure you have Docker and Docker Compose installed. You can run the entire stack locally using the provided `docker-compose.yml` file.

### Remote Development
For remote development, you can connect to the PostgreSQL and Hive services using DBeaver or any SQL client that supports JDBC connections. Ensure your local machine can access the Docker host's IP address.

### CI/CD Integration
For CI/CD integration, consider using GitHub Actions or GitLab CI to automate testing and deployment of your data pipelines. You can set up workflows to run pre-commit hooks, validate SQL scripts, and deploy changes to your data infrastructure.

## 📚 Documentation
For more detailed documentation on each component, refer to the official documentation:
- [Hive Documentation](https://cwiki.apache.org/confluence/display/Hive/Home)
- [Hadoop Documentation](https://hadoop.apache.org/docs/stable/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [DBeaver Documentation](https://dbeaver.com/docs/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [Black Documentation](https://black.readthedocs.io/en/stable/)
- [Isort Documentation](https://pycqa.github.io/isort/)
- [YAML Lint Documentation](https://yamllint.readthedocs.io/en/stable/)

### 🚀 Future Enhancements
Next steps could include:
- Adding Airflow for orchestration
- Streaming flight data with Kafka
- Dashboarding with Superset

### 🙌 Credits & Future Ideas
Built by @anderdam — powered by terminal rage and a helpful AI 😅

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📞 Contact
For questions or contributions, please open an issue or PR on GitHub.
��